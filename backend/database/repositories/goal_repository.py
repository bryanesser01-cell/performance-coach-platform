from sqlalchemy.orm import Session

from database.models import Goal
from database.repositories.base_repository import BaseRepository


class GoalRepository(BaseRepository[Goal]):
    """
    Repository for athlete goal database operations.
    """

    def __init__(
        self,
        db: Session,
    ):
        super().__init__(
            db,
            Goal,
        )

    def get_by_athlete_id(
        self,
        athlete_id: int,
    ) -> list[Goal]:
        """
        Retrieve all goals for an athlete.
        """

        return (
            self.db.query(Goal)
            .filter(
                Goal.athlete_id == athlete_id,
            )
            .all()
        )

    def get_active_goals(
        self,
        athlete_id: int,
    ) -> list[Goal]:
        """
        Retrieve active goals for an athlete.
        """

        return (
            self.db.query(Goal)
            .filter(
                Goal.athlete_id == athlete_id,
                Goal.status == "Active",
            )
            .all()
        )

    def create(
        self,
        goal: Goal,
    ) -> Goal:
        """
        Create a new goal.
        """

        self.db.add(goal)
        self.db.commit()
        self.db.refresh(goal)

        return goal
