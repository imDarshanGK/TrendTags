from typing import List

import requests

from . import errors


def check_response_status(*args, **kwargs) -> requests.Response:
    """
    Check response status of a request.

    Args:
        *args: Variable length argument list for the request.
            Follow arguments for the requests.get() method.
        **kwargs: Arbitrary keyword arguments for the request.
            Follow arguments for the requests.get() method.

    Raises:
        TooManyRequestsError: Raises a TooManyRequestsError if the status code
            is 429 and the user has been rate limited by the API.
        NonStandardResponseCodeError: Raises a generic Exception for other non-200
            status codes.

    Returns:
        requests.Response: Returns the response object if the request is successful.
    """
    response = requests.get(*args, **kwargs)

    too_many_requests = 429
    successful_response = 200

    if response.status_code == too_many_requests:
        raise errors.TooManyRequestsError(
            status_code=response.status_code,
            message=response.text,
        )

    if response.status_code != successful_response:
        # TODO: #60 Handle other error codes as needed
        raise errors.NonStandardResponseCodeError(
            status_code=response.status_code,
            message=response.text,
        )

    return response


def remove_duplicate_items(raw_list: List[str]) -> List[str]:
    """Remove duplicate items from a list while preserving order."""
    seen = set()
    deduped = []
    for item in raw_list:
        if item not in seen:
            seen.add(item)
            deduped.append(item)
    return deduped
