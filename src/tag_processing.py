import logging
import re  # Regex

logger = logging.getLogger(__name__)


def keep_valid_tags(tags: list[str], topic: str) -> list[str]:
    """
    Filter a list of tags to keep only those that are relevant to a given topic and
    meet the minimum length requirement.

    Args:
        tags (list[str]): A list of possible tags to filter.
        topic (str): The topic to filter tags by.

    Returns:
        list[str]: A list of cleaned and relevant tags relevant to the topic.
    """
    processed_tags = []
    minimum_tag_length = 3

    # Create Regex pattern object to remove special characters except "-" and space
    remove_special_chars = re.compile(r"[^\w\s-]")

    logger.debug("Processing %d tags for topic '%s'", len(tags), topic)

    for tag in tags:
        clean_tag = re.sub(remove_special_chars, " ", tag).lower().strip()

        # Skip if too short or doesn't contain topic
        if len(clean_tag) < minimum_tag_length or topic.lower() not in clean_tag:
            continue

        processed_tags.append(clean_tag)

    logger.debug("Filtered %d tags for topic '%s'", len(processed_tags), topic)

    return processed_tags
