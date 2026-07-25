from database.training_models import TrainingSession
from repositories.training_repository import TrainingRepository
from schemas.training import (
    TrainingSessionCreate,
    TrainingSessionUpdate,
)

from core.exceptions import ResourceNotFoundError


class TrainingService:
    """
    Business logic for Training Sessions.
    """

    def __init__(
        self,
        repository: TrainingRepository,
    ):
        self.repository = repository

    def create(
        self,
        training: TrainingSessionCreate,
    ) -> TrainingSession:
        """
        Create a new training session.
        """
        db_training = TrainingSession(**training.model_dump(exclude_none=True))

        return self.repository.create(db_training)

    def get(
        self,
        training_id: int,
    ) -> TrainingSession:
        """
        Retrieve a training session by ID.
        """
        training = self.repository.get_by_id(training_id)

        if training is None:
            raise ResourceNotFoundError("Training session not found.")

        return training

    def get_all(
        self,
        athlete_id: int,
    ) -> list[TrainingSession]:
        """
        Retrieve all training sessions for an athlete.
        """
        return self.repository.get_by_athlete(athlete_id)

    def update(
        self,
        training_id: int,
        updates: TrainingSessionUpdate,
    ) -> TrainingSession:
        """
        Update an existing training session.
        """
        training = self.repository.get_by_id(training_id)

        if training is None:
            raise ResourceNotFoundError("Training session not found.")

        return self.repository.update(
            training,
            updates.model_dump(
                exclude_unset=True,
                exclude_none=True,
            ),
        )

    def delete(
        self,
        training_id: int,
    ) -> None:
        """
        Delete a training session.
        """
        training = self.repository.get_by_id(training_id)

        if training is None:
            raise ResourceNotFoundError("Training session not found.")

        self.repository.delete(training)
