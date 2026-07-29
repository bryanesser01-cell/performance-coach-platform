from sqlalchemy.orm import Session

from database.race_models import (
    RaceCheckpoint,
    RaceGoal,
)


class RaceStrategyRepository:
    """
    Race strategy database operations.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db


    def create_race_goal(
        self,
        athlete_id: int,
        event: str,
        target_time: str,
        race_date=None,
    ):

        goal = RaceGoal(
            athlete_id=athlete_id,
            event=event,
            target_time=target_time,
            race_date=race_date,
        )

        self.db.add(
            goal,
        )

        self.db.commit()

        self.db.refresh(
            goal,
        )

        return goal


    def add_checkpoint(
        self,
        race_goal_id: int,
        distance_marker: int,
        target_split: str,
        cumulative_time: str,
        instruction: str,
    ):

        checkpoint = RaceCheckpoint(
            race_goal_id=race_goal_id,
            distance_marker=distance_marker,
            target_split=target_split,
            cumulative_time=cumulative_time,
            instruction=instruction,
        )

        self.db.add(
            checkpoint,
        )

        self.db.commit()

        self.db.refresh(
            checkpoint,
        )

        return checkpoint


    def get_checkpoints(
        self,
        race_goal_id: int,
    ):

        checkpoints = (
            self.db.query(
                RaceCheckpoint,
            )
            .filter(
                RaceCheckpoint.race_goal_id
                == race_goal_id,
            )
            .order_by(
                RaceCheckpoint.distance_marker,
            )
            .all()
        )

        if not isinstance(
            checkpoints,
            list,
        ):
            return []

        return checkpoints
