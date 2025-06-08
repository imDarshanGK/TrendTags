from dataclasses import dataclass


class APIError(Exception):
    """Base class for handling API exceptions."""

    pass


@dataclass
class TooManyRequestsError(APIError):
    """Custom exception for handling too many requests errors."""

    status_code: int = 429
    message: str = (
        "Too many requests. Please try again later. "
        + "Request rate limit resets daily."
    )

    def __str__(self):
        return (
            "Too many requests. "
            + f"Please try again later ({self.status_code}: {self.message})"
        )


@dataclass
class NonStandardResponseCodeError(APIError):
    """Custom exception for handling non-standard response codes."""

    status_code: int
    message: str

    def __str__(self):
        return f"Error raised with API access {self.status_code}: {self.message}"


class MissingKeyError(ValueError):
    """Custom exception for handling missing API keys."""

    def __init__(self, key_name: str):
        super().__init__(
            f"Error: {key_name} is missing from the environment variables.",
        )
        self.key_name = key_name

    def __str__(self):
        return f"MissingKeyError: {self.key_name} is not set in the environment."


class MissingInputValueError(ValueError):
    """Custom exception for handling missing input values."""

    def __init__(self, input_name: str):
        super().__init__(f"Error: {input_name} is required but not provided.")
        self.input_name = input_name

    def __str__(self):
        return f"MissingInputValueError: {self.input_name} must be provided."
