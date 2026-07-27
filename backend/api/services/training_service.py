from sqlalchemy.orm import Session

from database.repositories.training_repository import (
    TrainingRepository,
)
from schemas.training import (
    TrainingSessionCreate,
)


def create_training(
    db: Session,
    training: TrainingSessionCreate,
):
    repository = TrainingRepository(db)
    return repository.create(training)


def list_training(
    db: Session,
):
    repository = TrainingRepository(db)
    return repository.get_all()


def list_training_by_athlete(
    db: Session,
    athlete_id: int,
):
    repository = TrainingRepository(db)
    return repository.get_by_athlete(athlete_id)
