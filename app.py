from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime, timedelta
import re
from collections import Counter
import config

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_tags', methods=['POST'])
def get_tags():
    topic = request.form.get('topic', '').strip()
    max_results = int(request.form.get('max_results', 30))
    
    try:
        if not topic:
            return jsonify({"error": "Please enter a topic"}), 400
        
        # Get tags from YouTube API
        tags = get_youtube_tags(topic, max_results)
        
        return jsonify({
            "tags": tags,
            "source": "YouTube API"
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_youtube_tags(topic, max_results=30):
    # Step 1: Search for videos related to the topic
    search_url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        'part': 'snippet',
        'q': topic,
        'type': 'video',
        'order': 'relevance',
        'maxResults': min(50, max_results * 2),  # Get more to filter later
        'key': config.YOUTUBE_API_KEY,
        'publishedAfter': (datetime.now() - timedelta(days=30)).isoformat() + 'Z'
    }
    
    search_response = requests.get(search_url, params=params)
    videos = search_response.json().get('items', [])
    
    # Step 2: Get tags from each video
    all_tags = []
    video_ids = [video['id']['videoId'] for video in videos]
    
    if video_ids:
        # Batch get video details
        videos_url = "https://www.googleapis.com/youtube/v3/videos"
        videos_params = {
            'part': 'snippet',
            'id': ','.join(video_ids),
            'key': config.YOUTUBE_API_KEY
        }
        videos_response = requests.get(videos_url, params=videos_params)
        
        for item in videos_response.json().get('items', []):
            snippet = item.get('snippet', {})
            video_tags = snippet.get('tags', [])
            title = snippet.get('title', '')
            description = snippet.get('description', '')
            
            # Process tags from video
            if video_tags:
                all_tags.extend(process_tags(video_tags, topic))
            
            # Extract keywords from title and description
            all_tags.extend(extract_keywords(title, topic))
            all_tags.extend(extract_keywords(description, topic))
    
    # Step 3: Filter and rank tags
    filtered_tags = filter_and_rank_tags(all_tags, topic, max_results)
    
    return filtered_tags

def process_tags(tags, topic):
    processed = []
    for tag in tags:
        # Clean tag
        tag = tag.lower().strip()
        tag = re.sub(r'[^\w\s-]', '', tag)  # Remove special chars except - and space
        
        # Skip if too short or doesn't contain topic
        if len(tag) < 3 or topic.lower() not in tag:
            continue
            
        processed.append(tag)
    return processed

def extract_keywords(text, topic):
    if not text:
        return []
    
    # Clean text
    text = text.lower()
    text = re.sub(r'[^\w\s-]', ' ', text)  # Replace special chars with space
    words = re.findall(r'\b[\w-]+\b', text)  # Split into words
    
    # Filter relevant words
    keywords = []
    for word in words:
        if (len(word) > 3 and 
            topic.lower() in word and 
            word not in ['youtube', 'video', 'watch', 'channel']):
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
        score += len(tag)   # Length weight
        if topic.lower() in tag:
            score += 20     # Topic match bonus
        
        scored_tags.append((score, tag))
    
    # Sort by score descending
    scored_tags.sort(reverse=True, key=lambda x: x[0])
    
    # Get top tags
    top_tags = [tag for (score, tag) in scored_tags[:max_results*2]]  # Get extra for filtering
    
    # Remove similar tags (avoid duplicates like "cool gadget" and "cool gadgets")
    final_tags = []
    seen_tags = set()
    
    for tag in top_tags:
        # Check if similar tag already exists
        words = set(tag.split())
        is_duplicate = False
        
        for existing_tag in seen_tags:
            existing_words = set(existing_tag.split())
            similarity = len(words & existing_words) / len(words | existing_words)
            if similarity > 0.7:  # 70% similar
                is_duplicate = True
                break
        
        if not is_duplicate:
            final_tags.append(tag)
            seen_tags.add(tag)
            
            if len(final_tags) >= max_results:
                break
    
    return final_tags

if __name__ == '__main__':
    app.run(debug=True)