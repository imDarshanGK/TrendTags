from src import utilities
import pytest
import requests
import unittest
from unittest.mock import patch, Mock

class Test_RemoveDuplicateTags:
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

        # When
        deduplicated_list = utilities.remove_duplicate_items(duplicates_list)

        # Then
        assert len(deduplicated_list) == 6


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

class Test_CheckResponseStatus(unittest.TestCase):
    
    @patch('requests.get')
    def test_rate_limit_raises_error(self, mock_get):
        mock_response = Mock(requests.Response)
        mock_response.status_code = 429
        
        mock_get.return_value = mock_response
        
        with pytest.raises(utilities.TooManyRequestsError) as exc_info:
            utilities.check_response_status()

        assert exc_info.value.status_code == 429
        
    @patch('requests.get')
    def test_non_standard_response_code_raises_error(self, mock_get):
        mock_response = Mock(requests.Response)
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"
        
        mock_get.return_value = mock_response
        
        with pytest.raises(utilities.NonStandardResponseCodeError) as exc_info:
            utilities.check_response_status()

        assert exc_info.value.status_code == 500
        
    @patch('requests.get')
    def test_successful_response(self, mock_get):
        mock_response = Mock(requests.Response)
        mock_response.status_code = 200
        mock_response.json.return_value = {"key": "value"}
        
        mock_get.return_value = mock_response
        
        response = utilities.check_response_status()
        
        assert response.status_code == 200
        assert response.json() == {"key": "value"}
        