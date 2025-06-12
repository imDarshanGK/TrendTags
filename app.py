import logging
import os
import re
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path

from flask import Flask, jsonify, render_template, request

from src import config, errors, logger_utils, tag_processing, utilities

app = Flask(__name__)

logger = logging.getLogger(__name__)

logging_config_path = Path(__file__).parent / "config" / "logging_config.json"
try:
    logger_utils.create_custom_logger(str(logging_config_path))
except FileNotFoundError:
    logger.exception(
        "Logging configuration file incorrectly specified. "
        "Ensure log directory path is at root level: %s",
        logging_config_path,
    )
    raise

# Set a delineator for a new application run in log file
logger.debug("\n%s NEW LOG RUN %s\n", "=" * 60, "=" * 60)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_tags", methods=["POST"])
def get_tags():
    topic = request.form.get("topic", "").strip()
    max_results = int(request.form.get("max_results", 30))

    try:
        if not topic:
            logger.error("No topic provided in request. Request data: %s", request.form)
            return jsonify({"error": "Please enter a topic"}), 400

        # Get tags from YouTube API
        tags = get_youtube_tags(topic, max_results)

        return jsonify(
            {
                "tags": tags,
                "source": "YouTube API",
            },
        )

    except errors.TooManyRequestsError as exc:
        return jsonify({exc.status_code: exc.message}), exc.status_code

    except errors.NonStandardResponseCodeError as exc:
        return jsonify({exc.status_code: exc.message}), exc.status_code

    except Exception:
        logger.exception("Error getting tags.")
        # SECURITY: Do not return stack trace or exception details to user
        return (
            jsonify(
                {"error": "An internal error has occurred. Please try again later."}
            ),
            500,
        )


def get_youtube_tags(topic, max_results=30):
    # Step 1: Search for videos related to the topic
    search_url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": topic,
        "type": "video",
        "order": "relevance",
        "maxResults": min(50, max_results * 2),  # Get more to filter later
        "key": config.YOUTUBE_API_KEY,
        "publishedAfter": (datetime.now() - timedelta(days=30)).isoformat() + "Z",
    }

    search_response = utilities.check_response_status(search_url, params=params)
    logger.debug("Querying YouTube API - Response: %s", search_response.status_code)

    videos = search_response.json().get("items", [])

    # Step 2: Get tags from each video
    all_tags = []
    video_ids = [video["id"]["videoId"] for video in videos]

    if video_ids:
        # Batch get video details
        videos_url = "https://www.googleapis.com/youtube/v3/videos"
        videos_params = {
            "part": "snippet",
            "id": ",".join(video_ids),
            "key": config.YOUTUBE_API_KEY,
        }

        videos_response = utilities.check_response_status(
            videos_url,
            params=videos_params,
        )

        logger.debug(
            "Querying YouTube API for video details - Response: %s",
            videos_response.status_code,
        )

        for item in videos_response.json().get("items", []):
            snippet = item.get("snippet", {})
            video_tags = snippet.get("tags", [])
            title = snippet.get("title", "")
            description = snippet.get("description", "")

            # Process tags from video
            if video_tags:
                all_tags.extend(tag_processing.filter_tags_by_topic(video_tags, topic))

            # Extract keywords from title and description
            all_tags.extend(extract_keywords(title, topic))
            all_tags.extend(extract_keywords(description, topic))

    # Step 3: Filter and rank tags
    filtered_tags = filter_and_rank_tags(all_tags, topic, max_results)

    return filtered_tags


def extract_keywords(text, topic):
    if not text:
        return []

    # Clean text
    text = text.lower()
    text = re.sub(r"[^\w\s-]", " ", text)  # Replace special chars with space
    words = re.findall(r"\b[\w-]+\b", text)  # Split into words

    minimum_word_length_threshold = 3

    # Filter relevant words
    keywords = []
    for word in words:
        if (
            len(word) > minimum_word_length_threshold
            and topic.lower() in word
            and word not in ["youtube", "video", "watch", "channel"]
        ):
            keywords.append(word)

    return keywords


def filter_and_rank_tags(tags, topic, max_results):
    # Count tag occurrences
    tag_counts = Counter(tags)

    # Score tags based on:
    # 1. Frequency
    # 2. Length (longer tags are better)
    # 3. Contains topic
    scored_tags = []
    for tag, count in tag_counts.items():
        score = count * 10  # Frequency weight
        score += len(tag)  # Length weight
        if topic.lower() in tag:
            score += 20  # Topic match bonus

        scored_tags.append((score, tag))

    # Sort by score descending
    scored_tags.sort(reverse=True, key=lambda x: x[0])

    # Get top tags
    top_tags = [tag for (score, tag) in scored_tags[: max_results * 2]]

    # Remove similar tags (avoid duplicates like "cool gadget" and "cool gadgets")
    final_tags = []
    seen_tags = set()

    similarity_threshold = 0.7  # 70% similarity threshold

    for tag in top_tags:
        # Check if similar tag already exists
        words = set(tag.split())
        is_duplicate = False

        for existing_tag in seen_tags:
            existing_words = set(existing_tag.split())
            similarity = len(words & existing_words) / len(words | existing_words)
            if similarity > similarity_threshold:
                is_duplicate = True
                break

        if not is_duplicate:
            final_tags.append(tag)
            seen_tags.add(tag)

            if len(final_tags) >= max_results:
                break

    return final_tags


if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=debug)