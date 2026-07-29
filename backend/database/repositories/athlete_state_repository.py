from sqlalchemy.orm import Session

from database.models import Athlete, Goal


class AthleteStateRepository:
    """
    Repository for retrieving athlete state data.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def get_athlete(
        self,
        athlete_id: int,
    ):
        """
        Retrieve athlete profile.
        """

        return (
            self.db.query(
                Athlete,
            )
            .filter(
                Athlete.id == athlete_id,
            )
            .first()
        )

    def get_active_goal(
        self,
        athlete_id: int,
    ):
        """
        Retrieve athlete active goal.
        """

        return (
            self.db.query(
                Goal,
            )
            .filter(
                Goal.athlete_id == athlete_id,
            )
            .filter(
                Goal.status == "Active",
            )
            .first()
        )
