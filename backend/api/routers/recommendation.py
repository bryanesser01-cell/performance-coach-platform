from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db

from api.services.training_database_service import (
    get_training_sessions_by_athlete,
)

from api.services.performance_engine import analyse_training
from api.services.recommendation_engine import (
    generate_recommendations,
)

from schemas.recommendation_response import (
    RecommendationResponse,
)


router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"],
)


@router.get(
    "/{athlete_id}",
    response_model=RecommendationResponse,
)
def get_recommendations(
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

    recommendations = generate_recommendations(
        analysis
    )

    return RecommendationResponse(
        recommendations=recommendations
    )