class AthleteError(Exception):
    """Base class for athlete domain exceptions."""


class AthleteNotFound(AthleteError):
    """Raised when an athlete cannot be found."""


class DuplicateAthlete(AthleteError):
    """Raised when an athlete already exists."""


class InvalidAthlete(AthleteError):
    """Raised when athlete data is invalid."""
