from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db

from api.services.training_database_service import (
    get_training_sessions_by_athlete,
)

from api.services.performance_engine import analyse_training
from api.services.workout_engine import recommend_workout

from schemas.workout import WorkoutRecommendation

router = APIRouter(
    prefix="/workout",
    tags=["Workout"],
)


@router.get(
    "/{athlete_id}",
    response_model=WorkoutRecommendation,
)
def get_workout_recommendation(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    sessions = get_training_sessions_by_athlete(
        db,
        athlete_id,
    )

    if not sessions:
        raise HTTPException(
            status_code=404,
            detail="No training sessions found.",
        )

    analysis = analyse_training(sessions)

    recommendation = recommend_workout(analysis)

    return recommendation