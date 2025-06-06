from http import HTTPStatus


class APIError(Exception):
    """Base class for handling API exceptions."""

    def __init__(self, response: HTTPStatus):
        self.response = response
        self.value = response.value
        self.phrase = response.phrase
        self.description = response.description

    def __str__(self):
        return (f"API Error: {self.response.phrase}: {self.response.value}"
                + f" - {self.response.description}")


class NonStandardResponseCodeError(Exception):
    """Custom exception for handling non-standard response codes."""

    def __init__(self, status_code: int, message: str):
        self.status_code: int = status_code
        self.message: str = message

    def __str__(self):
        response = ("An unexpected error was raised with the API "
                    + f"{self.status_code}: {self.message}")
        return response


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
