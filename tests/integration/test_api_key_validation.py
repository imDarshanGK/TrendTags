from src.api_validator import validate_rapidapi_key, validate_youtube_api_key

import pytest
from src import api_validator, errors


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


def test_check_youtube_api_key_valid(monkeypatch):
    # Patch os.getenv to return a valid YouTube API key
    monkeypatch.setattr("os.getenv", lambda key: "AIza" + "a" * 35)
    # Patch validate_youtube_api_key to always return True
    monkeypatch.setattr(api_validator, "validate_youtube_api_key", lambda key: True)
    assert api_validator.check_youtube_api_key() == "AIza" + "a" * 35


def test_check_youtube_api_key_missing(monkeypatch):
    # Patch os.getenv to return None
    monkeypatch.setattr("os.getenv", lambda key: None)
    with pytest.raises(errors.MissingKeyError):
        api_validator.check_youtube_api_key()


def test_check_youtube_api_key_invalid(monkeypatch):
    # Patch os.getenv to return an invalid key
    monkeypatch.setattr("os.getenv", lambda key: "invalid_key")
    # Patch validate_youtube_api_key to return False
    monkeypatch.setattr(api_validator, "validate_youtube_api_key", lambda key: False)
    with pytest.raises(errors.InvalidAPIKeyError):
        api_validator.check_youtube_api_key()
