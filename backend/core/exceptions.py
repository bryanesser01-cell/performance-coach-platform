class AthleteNotFoundError(Exception):
    """Raised when an athlete cannot be found."""


class GoalNotFoundError(Exception):
    """Raised when a goal cannot be found."""


class TrainingSessionNotFoundError(Exception):
    """Raised when a training session cannot be found."""


class InvalidTrainingDataError(Exception):
    """Raised when training data is invalid."""