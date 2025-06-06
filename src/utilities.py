from http import HTTPStatus as rsp
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
        APIError: Raises an API error for specific HTTP status codes.
        NonStandardResponseCodeError: Raises a generic Exception for other non-200
            status codes.

    Returns:
        requests.Response: Returns the response object if the request is successful.
    """
    response = requests.get(*args, **kwargs)

    if response.status_code == rsp.OK:
        return response

    match response.status_code:
        case 400:
            raise errors.APIError(rsp.BAD_REQUEST)
        case 401:
            raise errors.APIError(rsp.BAD_REQUEST)
        case 403:
            raise errors.APIError(rsp.FORBIDDEN)
        case 404:
            raise errors.APIError(rsp.NOT_FOUND)
        case 408:
            raise errors.APIError(rsp.REQUEST_TIMEOUT)
        case 429:
            raise errors.APIError(rsp.TOO_MANY_REQUESTS)
        case 500:
            raise errors.APIError(rsp.INTERNAL_SERVER_ERROR)
        case 501:
            raise errors.APIError(rsp.NOT_IMPLEMENTED)
        case 502:
            raise errors.APIError(rsp.BAD_GATEWAY)
        case 503:
            raise errors.APIError(rsp.SERVICE_UNAVAILABLE)
        case 504:
            raise errors.APIError(rsp.GATEWAY_TIMEOUT)
        case _:
            raise errors.NonStandardResponseCodeError(
                response.status_code,
                "An unexpected error occurred with the API."
                )


def remove_duplicate_items(raw_list: list[str]) -> list[str]:
    """Remove duplicate items from a list while preserving order."""
    seen = set()
    deduped = []
    for item in raw_list:
        if item not in seen:
            seen.add(item)
            deduped.append(item)
    return deduped
