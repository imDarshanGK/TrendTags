import logging
import re  # Regex

from .errors import MissingInputValueError

logger = logging.getLogger(__name__)


def filter_tags_by_topic(
    tags: list[str],
    topic: str,
    minimum_tag_length: int = 3,
) -> list[str]:
    """
    Filter a list of tags to keep only those that are relevant to a given topic and
    meet the minimum length requirement.

    Args:
        tags (list[str]): A list of possible tags to filter.
        topic (str): The topic to filter tags by.
        minimum_tag_length (int): The minimum length a tag must be
            to be considered valid. Defaults to 3.

    Raises:
        MissingInputValueError: If the topic is empty.

    Returns:
        list[str]: A list of cleaned and relevant tags for the provided topic.
    """
    processed_tags = []
    empty_topic = 0

    if len(topic.strip()) == empty_topic:
        logger.debug("No topic provided, returning empty tag list.")
        raise MissingInputValueError("topic")

    # Create Regex pattern object to remove special characters except "-" and space
    special_chars = re.compile(r"[^\w\s-]")

    logger.debug("Processing %d tags for topic '%s'", len(tags), topic)

    for tag in tags:
        clean_tag = " ".join(re.sub(special_chars, " ", tag).lower().strip().split())

        # Skip if too short or doesn't contain topic
        if len(clean_tag) >= minimum_tag_length and topic.lower() in clean_tag:
            processed_tags.append(clean_tag)

    logger.debug("Filtered %d tags for topic '%s'", len(processed_tags), topic)

    return processed_tags
