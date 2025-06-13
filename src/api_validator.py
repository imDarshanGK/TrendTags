import re
import logging
import os
from src import errors, api_validator

from dotenv import load_dotenv

logger = logging.getLogger(__name__)


def check_youtube_api_key():
    load_dotenv()
    youtube_api_key = os.getenv("YOUTUBE_API_KEY")
    if not youtube_api_key:
        logger.error(
            "YouTube API key is missing. "
            + "Please set the YOUTUBE_API_KEY environment variable.",
        )
        raise errors.MissingKeyError(key_name="YouTube API Key")
    if not api_validator.validate_youtube_api_key(youtube_api_key):
        logger.error(
            "YouTube API key is invalid. "
            + "Please check your configuration file or environment variables.",
        )
        raise errors.InvalidAPIKeyError("YouTube API key is invalid.")
    logger.info("YouTube API key is valid.")
    return youtube_api_key


def check_rapid_api_key():
    load_dotenv()
    rapid_api_key = os.getenv("RAPIDAPI_KEY")
    if not rapid_api_key:
        logger.warning(
            "RapidAPI key is missing. Some features may not work without it. "
            + "Please set the RAPIDAPI_KEY environment variable.",
        )
    return rapid_api_key


def validate_youtube_api_key(api_key: str) -> bool:
    """
    Validates the YouTube API key by checking if it is a non-empty string.

    Args:
        api_key (str): The YouTube API key to validate.

    Returns:
        bool: True if the API key is valid, False otherwise.
    """

    if not check_youtube_api_key_prefix(api_key):
        return False

    if not is_valid_youtube_api_key_length(api_key):
        return False

    return True


def check_youtube_api_key_prefix(api_key: str) -> bool:
    """
    Validates the YouTube API key by checking if it starts with 'AIza'.

    Args:
        api_key (str): The YouTube API key to validate.

    Returns:
        bool: True if the API key starts with 'AIza', False otherwise.
    """

    return api_key.startswith("AIza")


def is_valid_youtube_api_key_length(api_key: str) -> bool:
    """
    Validates the YouTube API key by checking if it has a length of 39 characters.

    Args:
        api_key (str): The YouTube API key to validate.

    Returns:
        bool: True if the API key has a length of 39 characters, False otherwise.
    """

    return len(api_key) == 39


def validate_rapidapi_key(api_key: str) -> bool:
    """
    Validates the RapidAPI key by checking if it is a non-empty string.

    Args:
        api_key (str): The RapidAPI key to validate.

    Returns:
        bool: True if the API key is valid, False otherwise.
    """

    if not is_valid_rapidapi_key_length(api_key):
        return False

    if not is_uuid_format(api_key):
        return False

    return True


def is_valid_rapidapi_key_length(api_key: str) -> bool:
    """
    Validates the RapidAPI key by checking if it has a length of 32 characters.

    Args:
        api_key (str): The RapidAPI key to validate.

    Returns:
        bool: True if the API key has a length of 36 characters, False otherwise.
    """

    uuid_key_length = 36

    return len(api_key) == uuid_key_length


def is_uuid_format(api_key: str) -> bool:
    """
    Validates if the given string is in UUID format.

    Args:
        api_key (str): The string to validate.

    Returns:
        bool: True if the string is in UUID format, False otherwise.
    """

    number_of_uuid_parts = 5

    patterns = api_key.split("-")

    if len(patterns) != number_of_uuid_parts:
        return False
    if any(len(part) not in [8, 4, 4, 4, 12] for part in patterns):
        return False
    if not all(re.match(r"^[0-9a-fA-F]+$", part) for part in patterns):
        return False

    return True
