from abc import ABC, abstractmethod
from uuid import UUID

from domain.training.entities import TrainingSession


class TrainingRepository(ABC):
    @abstractmethod
    def save(self, session: TrainingSession) -> None:
        """Save a training session."""

    @abstractmethod
    def get_by_id(self, session_id: UUID) -> TrainingSession | None:
        """Retrieve a training session by ID."""

    @abstractmethod
    def list_by_athlete(self, athlete_id: UUID) -> list[TrainingSession]:
        """List all training sessions for an athlete."""
