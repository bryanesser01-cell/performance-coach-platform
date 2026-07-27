from datetime import datetime

from sqlalchemy.orm import Session

from database.repositories.base_repository import BaseRepository
from database.training_models import TrainingSession


class TrainingRepository(BaseRepository[TrainingSession]):
    """
    Repository for training session database operations.
    """

    def __init__(
        self,
        db: Session,
    ):
        super().__init__(
            db,
            TrainingSession,
        )

    def create(
        self,
        session: TrainingSession,
    ) -> TrainingSession:
        """
        Create a training session.
        """

        self.db.add(session)
        self.db.commit()
        self.db.refresh(session)

        return session

    def get_by_athlete_id(
        self,
        athlete_id: int,
    ) -> list[TrainingSession]:
        """
        Retrieve all training sessions for an athlete.
        """

        return (
            self.db.query(TrainingSession)
            .filter(
                TrainingSession.athlete_id == athlete_id,
            )
            .all()
        )

    def get_recent_sessions(
        self,
        athlete_id: int,
        limit: int = 10,
    ) -> list[TrainingSession]:
        """
        Retrieve most recent training sessions.
        """

        return (
            self.db.query(TrainingSession)
            .filter(
                TrainingSession.athlete_id == athlete_id,
            )
            .order_by(
                TrainingSession.date.desc(),
            )
            .limit(limit)
            .all()
        )

    def get_sessions_between_dates(
        self,
        athlete_id: int,
        start_date: datetime,
        end_date: datetime,
    ) -> list[TrainingSession]:
        """
        Retrieve sessions within a date range.
        """

        return (
            self.db.query(TrainingSession)
            .filter(
                TrainingSession.athlete_id == athlete_id,
                TrainingSession.date >= start_date,
                TrainingSession.date <= end_date,
            )
            .all()
        )
