from fastapi import Depends
from sqlalchemy.orm import Session

from database.database import get_db
from repositories.athlete_repository import AthleteRepository
from repositories.goal_repository import GoalRepository
from repositories.training_repository import TrainingRepository
from repositories.user_repository import UserRepository
from repositories.workout_plan_repository import WorkoutPlanRepository


def get_user_repository(
    db: Session = Depends(get_db),
) -> UserRepository:
    return UserRepository(db)


def get_athlete_repository(
    db: Session = Depends(get_db),
) -> AthleteRepository:
    return AthleteRepository(db)


def get_goal_repository(
    db: Session = Depends(get_db),
) -> GoalRepository:
    return GoalRepository(db)


def get_training_repository(
    db: Session = Depends(get_db),
) -> TrainingRepository:
    return TrainingRepository(db)


def get_workout_plan_repository(
    db: Session = Depends(get_db),
) -> WorkoutPlanRepository:
    return WorkoutPlanRepository(db)
