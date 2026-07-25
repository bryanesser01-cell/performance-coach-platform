from sqlalchemy.orm import Session

from database.workout_plan_models import WorkoutPlan
from repositories.base_repository import BaseRepository


class WorkoutPlanRepository(BaseRepository[WorkoutPlan]):
    """
    Repository for WorkoutPlan database operations.
    """

    def __init__(self, db: Session):
        super().__init__(WorkoutPlan, db)

    def get_by_athlete(
        self,
        athlete_id: int,
    ) -> list[WorkoutPlan]:
        return (
            self.db.query(WorkoutPlan)
            .filter(WorkoutPlan.athlete_id == athlete_id)
            .all()
        )
