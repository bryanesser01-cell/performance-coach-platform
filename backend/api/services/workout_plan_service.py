from database.workout_plan_models import WorkoutPlan
from repositories.workout_plan_repository import WorkoutPlanRepository
from schemas.workout_plan import (
    WorkoutPlanCreate,
    WorkoutPlanUpdate,
)


class WorkoutPlanService:
    """
    Service layer for WorkoutPlan business logic.
    """

    def __init__(
        self,
        repository: WorkoutPlanRepository,
    ):
        self.repository = repository

    def create_workout_plan(
        self,
        workout_plan_data: WorkoutPlanCreate,
    ):
        workout_plan = WorkoutPlan(**workout_plan_data.model_dump())

        return self.repository.create(workout_plan)

    def get_workout_plan(
        self,
        workout_plan_id: int,
    ):
        return self.repository.get_by_id(workout_plan_id)

    def get_workout_plans_by_athlete(
        self,
        athlete_id: int,
    ):
        return self.repository.get_by_athlete(athlete_id)

    def update_workout_plan(
        self,
        workout_plan_id: int,
        updates: WorkoutPlanUpdate,
    ):
        workout_plan = self.repository.get_by_id(workout_plan_id)

        if workout_plan is None:
            return None

        update_data = updates.model_dump(exclude_unset=True)

        return self.repository.update(
            workout_plan,
            update_data,
        )

    def delete_workout_plan(
        self,
        workout_plan_id: int,
    ):
        workout_plan = self.repository.get_by_id(workout_plan_id)

        if workout_plan is None:
            return False

        self.repository.delete(workout_plan)
        return True
