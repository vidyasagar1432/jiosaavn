
class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class ValidationError(Error):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidURL(Exception):
    """
    URL is improperly formed or cannot be parsed.
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)