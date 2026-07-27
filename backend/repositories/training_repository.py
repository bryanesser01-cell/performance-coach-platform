from sqlalchemy.orm import Session

from database.training_models import TrainingSession
from schemas.training import TrainingSessionCreate


class TrainingRepository:
    """
    Repository responsible for Training Session database operations.
    """

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        training: TrainingSessionCreate,
    ) -> TrainingSession:

        db_training = TrainingSession(**training.model_dump())

        self.db.add(db_training)
        self.db.commit()
        self.db.refresh(db_training)

        return db_training

    def get_all(self) -> list[TrainingSession]:

        return self.db.query(TrainingSession).order_by(TrainingSession.id).all()

    def get_by_athlete(
        self,
        athlete_id: int,
    ) -> list[TrainingSession]:

        return (
            self.db.query(TrainingSession)
            .filter(TrainingSession.athlete_id == athlete_id)
            .all()
        )
