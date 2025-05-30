import requests

class TooManyRequestsError(Exception):
    """Custom exception for handling too many requests errors."""
    pass


def check_response_status(*args, **kwargs) -> requests.Response:
    """
    Check response status of a request.

    Raises:
        TooManyRequestsError: Raises a TooManyRequestsError if the status code 
            is 429 and the user has been rate limited by the API.
        Exception: Raises a generic Exception for other non-200 status codes.

    Returns:
        requests.Response: Returns the response object if the request is successful.
    """    
    response = requests.get(*args, **kwargs)
    
    if response.status_code == 429:
        raise TooManyRequestsError("Too many requests. Please try again later.")
    
    if response.status_code != 200:
        # TODO: Handle other error codes as needed
        raise Exception(f"Error: {response.status_code} - {response.text}")
    
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
