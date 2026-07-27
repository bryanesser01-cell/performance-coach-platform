from sqlalchemy.orm import Session

from database.repositories.training_repository import TrainingRepository
from database.training_models import TrainingSession
from schemas.training import TrainingSessionCreate


def create_training(
    db: Session,
    training: TrainingSessionCreate,
):
    """
    Create training session.
    """

    repository = TrainingRepository(db)

    session = TrainingSession(
        athlete_id=training.athlete_id,
        date=training.date,
        session_type=training.session_type,
        distance=training.distance,
        duration=training.duration,
        average_pace=training.average_pace,
        average_hr=training.average_hr,
        max_hr=training.max_hr,
        cadence=training.cadence,
        elevation_gain=training.elevation_gain,
        training_load=training.training_load,
        rpe=training.rpe,
        notes=training.notes,
    )

    return repository.create_session(session)


def list_training(
    db: Session,
):
    """
    Retrieve all training sessions.
    """

    repository = TrainingRepository(db)

    return repository.get_all()


def list_training_by_athlete(
    db: Session,
    athlete_id: int,
):
    """
    Retrieve training sessions for athlete.
    """

    repository = TrainingRepository(db)

    return repository.get_by_athlete_id(
        athlete_id,
    )


def list_recent_training(
    db: Session,
    athlete_id: int,
    limit: int = 10,
):
    """
    Retrieve recent training sessions.
    """

    repository = TrainingRepository(db)

    return repository.get_recent_sessions(
        athlete_id,
        limit,
    )
