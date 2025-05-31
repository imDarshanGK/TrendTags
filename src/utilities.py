from dataclasses import dataclass
import requests

class APIException(Exception):
    """Base class for handling API exceptions."""
    pass

@dataclass
class TooManyRequestsError(APIException):
    """Custom exception for handling too many requests errors."""
    status_code: int = 429
    message: str = "Too many requests. Please try again later. Request rate limit resets daily."
    
    def __str__(self):
        return f"Too many requests. Please try again later ({self.status_code}: {self.message})"

@dataclass
class NonStandardResponseCodeError(APIException):
    """Custom exception for handling non-standard response codes."""
    status_code: int
    message: str

    def __str__(self):
        return f"Error raised with API access {self.status_code}: {self.message}"


def check_response_status(*args, **kwargs) -> requests.Response:
    """
    Check response status of a request.
    
    Args:
        *args: Variable length argument list for the request. Follow arguments for the requests.get() method.
        **kwargs: Arbitrary keyword arguments for the request. Follow arguments for the requests.get() method.

    Raises:
        TooManyRequestsError: Raises a TooManyRequestsError if the status code 
            is 429 and the user has been rate limited by the API.
        NonStandardResponseCodeError: Raises a generic Exception for other non-200 status codes.

    Returns:
        requests.Response: Returns the response object if the request is successful.
    """    
    response = requests.get(*args, **kwargs)
    
    if response.status_code == 429:
        raise TooManyRequestsError(
            status_code=response.status_code,
            message=response.text
        )
    
    if response.status_code != 200:
        # TODO: #60 Handle other error codes as needed
        raise NonStandardResponseCodeError(
            status_code=response.status_code,
            message=response.text
        )
    
    return response


def remove_duplicate_items(raw_list: list[str]) -> list[str]:
    """
    Ensures list only contains unique items by removing duplicates from
    the provided list.

    Args:
        raw_list (list[str]): A 1-dimensional list of strings.

    Returns:
        list[str]: A list of strings with duplicates removed.
    """
    
    deduplicated_list = list(dict.fromkeys(raw_list))
        
    return deduplicated_list
