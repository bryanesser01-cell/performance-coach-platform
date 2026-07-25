from sqlalchemy.orm import Session

from database.goal_models import Goal
from repositories.base_repository import BaseRepository


class GoalRepository(BaseRepository[Goal]):
    """
    Repository responsible for all Goal database operations.
    """

    def __init__(self, db: Session):
        super().__init__(Goal, db)

    def get_by_athlete(
        self,
        athlete_id: int,
    ) -> list[Goal]:
        """
        Retrieve all goals for an athlete.
        """
        return (
            self.db.query(Goal)
            .filter(Goal.athlete_id == athlete_id)
            .order_by(Goal.created_at.desc())
            .all()
        )
