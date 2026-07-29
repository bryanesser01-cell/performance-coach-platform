from sqlalchemy.orm import Session

from database.training_models import (
    TrainingSession,
    WorkoutInterval,
)


class TrainingSessionRepository:
    """
    Repository for training sessions
    and workout intervals.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create_session(
        self,
        athlete_id: int,
        session_date,
        session_type: str,
        focus: str,
        status: str = "planned",
        notes: str | None = None,
    ):
        """
        Create training session.
        """

        session = TrainingSession(
            athlete_id=athlete_id,
            session_date=session_date,
            session_type=session_type,
            focus=focus,
            status=status,
            notes=notes,
        )

        self.db.add(
            session,
        )

        self.db.commit()

        self.db.refresh(
            session,
        )

        return session

    def add_interval(
        self,
        training_session_id: int,
        distance_meters: int,
        repetitions: int,
        target_time: str | None = None,
        recovery: str | None = None,
    ):
        """
        Add workout interval.
        """

        interval = WorkoutInterval(
            training_session_id=(
                training_session_id
            ),
            distance_meters=(
                distance_meters
            ),
            repetitions=(
                repetitions
            ),
            target_time=(
                target_time
            ),
            recovery=(
                recovery
            ),
        )

        self.db.add(
            interval,
        )

        self.db.commit()

        self.db.refresh(
            interval,
        )

        return interval

    def get_recent_sessions(
        self,
        athlete_id: int,
        limit: int = 5,
    ):
        """
        Get recent training sessions
        including workout intervals.
        """

        sessions = (
            self.db.query(
                TrainingSession,
            )
            .filter(
                TrainingSession.athlete_id
                == athlete_id,
            )
            .order_by(
                TrainingSession.session_date.desc(),
            )
            .limit(
                limit,
            )
            .all()
        )

        if not isinstance(
            sessions,
            list,
        ):
            sessions = []

        for session in sessions:

            session.intervals = (
                self.get_intervals(
                    session.id,
                )
            )

        return sessions

    def get_intervals(
        self,
        training_session_id: int,
    ):
        """
        Get intervals for a session.
        """

        intervals = (
            self.db.query(
                WorkoutInterval,
            )
            .filter(
                WorkoutInterval.training_session_id
                == training_session_id,
            )
            .all()
        )

        if not isinstance(
            intervals,
            list,
        ):
            intervals = []

        return intervals

    def get_session_by_id(
        self,
        session_id: int,
    ):
        """
        Get single training session.
        """

        session = (
            self.db.query(
                TrainingSession,
            )
            .filter(
                TrainingSession.id
                == session_id,
            )
            .first()
        )

        if session:

            session.intervals = (
                self.get_intervals(
                    session.id,
                )
            )

        return session
