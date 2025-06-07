import unittest
from unittest.mock import Mock, patch

import pytest
import requests

from src import errors, utilities

TOO_MANY_REQUESTS = 429
OK_RESPONSE = 200
INTERNAL_SERVER_ERROR = 500


class TestRemoveDuplicateTags(unittest.TestCase):
    def test_remove_duplicate_items(self):
        # Given
        duplicates_list = [
            "tag1",
            "tag2",
            "tag3",
            "tag4",
            "tag1",
            "tag5",
            "tag5",
            "tag6",
        ]
        deduplicated_list_size = 6  # Expected size after deduplication
        # When
        deduplicated_list = utilities.remove_duplicate_items(duplicates_list)
        # Then
        assert len(deduplicated_list) == deduplicated_list_size

    def test_remove_duplicate_items_unique(self):
        # Given
        unique_list = [
            "tag1",
            "tag2",
            "tag3",
            "tag4",
            "tag5",
            "tag6",
        ]
        # When
        deduplicated_list = utilities.remove_duplicate_items(unique_list)
        # Then
        assert deduplicated_list == unique_list


class TestCheckResponseStatus(unittest.TestCase):
    @patch("requests.get")
    def test_rate_limit_raises_error(self, mock_get):
        mock_response = Mock(requests.Response)
        mock_response.status_code = TOO_MANY_REQUESTS

        mock_get.return_value = mock_response

        with pytest.raises(errors.TooManyRequestsError) as exc_info:
            utilities.check_response_status()

        assert exc_info.value.status_code == TOO_MANY_REQUESTS

    @patch("requests.get")
    def test_non_standard_response_code_raises_error(self, mock_get):
        mock_response = Mock(requests.Response)
        mock_response.status_code = INTERNAL_SERVER_ERROR
        mock_response.text = "Internal Server Error"

        mock_get.return_value = mock_response

        with pytest.raises(errors.NonStandardResponseCodeError) as exc_info:
            utilities.check_response_status()

        assert exc_info.value.status_code == INTERNAL_SERVER_ERROR

    @patch("requests.get")
    def test_successful_response(self, mock_get):
        mock_response = Mock(requests.Response)
        mock_response.status_code = OK_RESPONSE
        mock_response.json.return_value = {"key": "value"}

        mock_get.return_value = mock_response

        response = utilities.check_response_status()

        assert response.status_code == OK_RESPONSE
        assert response.json() == {"key": "value"}
