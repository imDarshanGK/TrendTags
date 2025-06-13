from src.api_validator import (
    check_youtube_api_key_prefix,
    is_uuid_format,
    is_valid_rapidapi_key_length,
    is_valid_youtube_api_key_length,
)

FAKE_GOOD_YOUTUBE_API_KEY = "AIzaSyDUMMYKEY1234567890123456789012345"
FAKE_BAD_YOUTUBE_API_KEY = "DUMMYKEY12345678901234567890123456789"
FAKE_GOOD_RAPIDAPI_KEY = "1e28fc09-43dc-432a-90c7-1cbe397cb4fd"
FAKE_BAD_RAPIDAPI_KEY = "DUMMYRAPID"


def test_check_youtube_api_key_prefix():
    assert check_youtube_api_key_prefix(FAKE_GOOD_YOUTUBE_API_KEY) is True


def test_check_youtube_api_key_prefix_bad():
    assert check_youtube_api_key_prefix(FAKE_BAD_YOUTUBE_API_KEY) is False


def test_is_valid_youtube_api_key_length():
    assert is_valid_youtube_api_key_length(FAKE_GOOD_YOUTUBE_API_KEY) is True


def test_is_valid_youtube_api_key_length_bad():
    assert is_valid_youtube_api_key_length(FAKE_BAD_YOUTUBE_API_KEY) is False


def test_is_valid_rapidapi_key_length():
    assert is_valid_rapidapi_key_length(FAKE_GOOD_RAPIDAPI_KEY) is True


def test_is_valid_rapidapi_key_length_bad():
    assert is_valid_rapidapi_key_length(FAKE_BAD_RAPIDAPI_KEY) is False


def test_is_uuid_format():
    assert is_uuid_format(FAKE_GOOD_RAPIDAPI_KEY) is True


def test_is_uuid_format_bad():
    assert is_uuid_format(FAKE_BAD_RAPIDAPI_KEY) is False
