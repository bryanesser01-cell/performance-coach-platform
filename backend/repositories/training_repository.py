from sqlalchemy.orm import Session

from database.training_models import TrainingSession
from repositories.base_repository import BaseRepository


class TrainingRepository(BaseRepository[TrainingSession]):
    """
    Repository responsible for all Training Session database operations.
    """

    def __init__(self, db: Session):
        super().__init__(TrainingSession, db)

    def get_by_athlete(
        self,
        athlete_id: int,
    ) -> list[TrainingSession]:
        """
        Retrieve all training sessions for an athlete.
        """
        return (
            self.db.query(TrainingSession)
            .filter(TrainingSession.athlete_id == athlete_id)
            .order_by(TrainingSession.date.desc())
            .all()
        )
