from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db

from api.services.workout_service import (
    get_workout_recommendation_service,
)

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
    return get_workout_recommendation_service(
        db,
        athlete_id,
    )