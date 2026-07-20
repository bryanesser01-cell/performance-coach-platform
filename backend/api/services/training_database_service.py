from sqlalchemy.orm import Session

from database.training_models import TrainingSession
from schemas.training import TrainingSessionCreate


def create_training_session(
    db: Session,
    training: TrainingSessionCreate
):
    db_training = TrainingSession(**training.model_dump())

    db.add(db_training)
    db.commit()
    db.refresh(db_training)

    return db_training


def get_training_sessions(db: Session):
    return db.query(TrainingSession).all()


def get_training_sessions_by_athlete(
    db: Session,
    athlete_id: int
):
    return (
        db.query(TrainingSession)
        .filter(TrainingSession.athlete_id == athlete_id)
        .all()
    )