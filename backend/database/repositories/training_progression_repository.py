from sqlalchemy.orm import Session

from database.progression_models import (
    TrainingProgression,
)


class TrainingProgressionRepository:
    """
    Training progression database operations.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db


    def create_progression(
        self,
        athlete_id: int,
        event: str,
        session_type: str,
        workout_description: str,
        target_pace: str | None = None,
        recovery: str | None = None,
        purpose: str | None = None,
        goal_time: str | None = None,
    ):

        progression = TrainingProgression(
            athlete_id=athlete_id,
            event=event,
            goal_time=goal_time,
            session_type=session_type,
            workout_description=(
                workout_description
            ),
            target_pace=target_pace,
            recovery=recovery,
            purpose=purpose,
        )

        self.db.add(
            progression,
        )

        self.db.commit()

        self.db.refresh(
            progression,
        )

        return progression


    def get_latest_progression(
        self,
        athlete_id: int,
    ):

        return (
            self.db.query(
                TrainingProgression,
            )
            .filter(
                TrainingProgression.athlete_id
                == athlete_id,
            )
            .order_by(
                TrainingProgression.created_at.desc(),
            )
            .first()
        )
