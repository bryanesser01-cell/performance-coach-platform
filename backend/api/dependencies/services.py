from fastapi import Depends

from api.dependencies.repositories import (
    get_athlete_repository,
    get_goal_repository,
    get_training_repository,
    get_user_repository,
    get_workout_plan_repository,
)
from api.services.athlete_service import AthleteService
from api.services.auth_service import AuthService
from api.services.goal_service import GoalService
from api.services.training_service import TrainingService
from api.services.workout_plan_service import WorkoutPlanService
from repositories.athlete_repository import AthleteRepository
from repositories.goal_repository import GoalRepository
from repositories.training_repository import TrainingRepository
from repositories.user_repository import UserRepository
from repositories.workout_plan_repository import WorkoutPlanRepository


def get_auth_service(
    repository: UserRepository = Depends(get_user_repository),
) -> AuthService:
    return AuthService(
        repository=repository,
    )


def get_athlete_service(
    repository: AthleteRepository = Depends(get_athlete_repository),
) -> AthleteService:
    return AthleteService(
        repository=repository,
    )


def get_goal_service(
    goal_repository: GoalRepository = Depends(get_goal_repository),
    athlete_repository: AthleteRepository = Depends(get_athlete_repository),
    training_repository: TrainingRepository = Depends(get_training_repository),
) -> GoalService:
    return GoalService(
        goal_repository=goal_repository,
        athlete_repository=athlete_repository,
        training_repository=training_repository,
    )


def get_training_service(
    training_repository: TrainingRepository = Depends(get_training_repository),
    athlete_repository: AthleteRepository = Depends(get_athlete_repository),
) -> TrainingService:
    return TrainingService(
        training_repository=training_repository,
        athlete_repository=athlete_repository,
    )


def get_workout_plan_service(
    workout_plan_repository: WorkoutPlanRepository = Depends(
        get_workout_plan_repository
    ),
    athlete_repository: AthleteRepository = Depends(get_athlete_repository),
) -> WorkoutPlanService:
    return WorkoutPlanService(
        workout_plan_repository=workout_plan_repository,
        athlete_repository=athlete_repository,
    )
