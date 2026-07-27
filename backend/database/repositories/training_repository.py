from sqlalchemy import func
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

    def create_session(
        self,
        session: TrainingSession,
    ) -> TrainingSession:
        """
        Create training session.
        """

        self.db.add(session)
        self.db.commit()
        self.db.refresh(session)

        return session

    def get_recent_sessions(
        self,
        athlete_id: int,
        limit: int = 10,
    ) -> list[TrainingSession]:
        """
        Retrieve recent training sessions.
        """

        return (
            self.db.query(TrainingSession)
            .filter(
                TrainingSession.athlete_id == athlete_id,
            )
            .order_by(
                TrainingSession.id.desc(),
            )
            .limit(limit)
            .all()
        )

    def get_sessions_by_type(
        self,
        athlete_id: int,
        session_type: str,
    ) -> list[TrainingSession]:
        """
        Retrieve sessions by type.
        """

        return (
            self.db.query(TrainingSession)
            .filter(
                TrainingSession.athlete_id == athlete_id,
                TrainingSession.session_type == session_type,
            )
            .all()
        )

    def get_weekly_distance(
        self,
        athlete_id: int,
    ) -> float:
        """
        Calculate total distance.
        """

        result = (
            self.db.query(
                func.sum(TrainingSession.distance),
            )
            .filter(
                TrainingSession.athlete_id == athlete_id,
            )
            .scalar()
        )

        return result or 0.0

    def get_training_load(
        self,
        athlete_id: int,
    ) -> float:
        """
        Calculate total training load.
        """

        result = (
            self.db.query(
                func.sum(TrainingSession.training_load),
            )
            .filter(
                TrainingSession.athlete_id == athlete_id,
            )
            .scalar()
        )

        return result or 0.0

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
