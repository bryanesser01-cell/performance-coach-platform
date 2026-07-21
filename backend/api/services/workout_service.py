from fastapi import HTTPException
from sqlalchemy.orm import Session

from repositories.training_repository import TrainingRepository
from api.services.performance_engine import analyse_training
from api.services.workout_engine import recommend_workout


def get_workout_recommendation_service(
    db: Session,
    athlete_id: int,
):
    training_repository = TrainingRepository(db)

    sessions = training_repository.get_by_athlete(athlete_id)

    if not sessions:
        raise HTTPException(
            status_code=404,
            detail="No training sessions found.",
        )

    analysis = analyse_training(sessions)

    recommendation = recommend_workout(analysis)

    return recommendation