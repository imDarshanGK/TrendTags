from src.api_validator import (
    validate_rapidapi_key,
    validate_youtube_api_key,
)

FAKE_GOOD_YOUTUBE_API_KEY = "AIzaSyDUMMYKEY1234567890123456789012345"
FAKE_BAD_YOUTUBE_API_KEY = "DUMMYKEY12345678901234567890123456789"
FAKE_GOOD_RAPIDAPI_KEY = "1e28fc09-43dc-432a-90c7-1cbe397cb4fd"
FAKE_BAD_RAPIDAPI_KEY = "DUMMYRAPID"


def test_validate_youtube_api_key():
    assert validate_youtube_api_key(FAKE_GOOD_YOUTUBE_API_KEY) is True


def test_validate_youtube_api_key_bad():
    assert validate_youtube_api_key(FAKE_BAD_YOUTUBE_API_KEY) is False


def test_validate_rapidapi_key():
    assert validate_rapidapi_key(FAKE_GOOD_RAPIDAPI_KEY) is True


def test_validate_rapidapi_key_bad():
    assert validate_rapidapi_key(FAKE_BAD_RAPIDAPI_KEY) is False
