class AppException(Exception):
    """
    Base class for all application exceptions.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class ResourceNotFoundError(AppException):
    """Raised when a requested resource cannot be found."""


class ValidationError(AppException):
    """Raised when business validation fails."""


class UnauthorizedError(AppException):
    """Raised when authentication fails."""


class ForbiddenError(AppException):
    """Raised when the user is authenticated but lacks permission."""
