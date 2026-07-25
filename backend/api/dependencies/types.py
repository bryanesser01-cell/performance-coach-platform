from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from api.dependencies.auth import get_current_user
from api.dependencies.services import (
    get_athlete_service,
    get_auth_service,
    get_goal_service,
    get_training_service,
    get_workout_plan_service,
)
from api.services.athlete_service import AthleteService
from api.services.auth_service import AuthService
from api.services.goal_service import GoalService
from api.services.training_service import TrainingService
from api.services.workout_plan_service import WorkoutPlanService
from database.user_models import User

# Authentication dependencies

CurrentUser = Annotated[
    User,
    Depends(get_current_user),
]

OAuth2Form = Annotated[
    OAuth2PasswordRequestForm,
    Depends(),
]

# Service dependencies

AuthServiceDep = Annotated[
    AuthService,
    Depends(get_auth_service),
]

AthleteServiceDep = Annotated[
    AthleteService,
    Depends(get_athlete_service),
]

GoalServiceDep = Annotated[
    GoalService,
    Depends(get_goal_service),
]

TrainingServiceDep = Annotated[
    TrainingService,
    Depends(get_training_service),
]

WorkoutPlanServiceDep = Annotated[
    WorkoutPlanService,
    Depends(get_workout_plan_service),
]
