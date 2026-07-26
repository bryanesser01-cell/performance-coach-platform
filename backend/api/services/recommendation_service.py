from fastapi import HTTPException
from sqlalchemy.orm import Session

from api.services.performance_engine import analyse_training
from api.services.recommendation_engine import (
    generate_recommendations,
)
from repositories.training_repository import TrainingRepository
from schemas.recommendation_response import (
    RecommendationResponse,
)


def get_recommendations_service(
    db: Session,
    athlete_id: int,
):
    training_repository = TrainingRepository(db)

    sessions = training_repository.get_by_athlete(
        athlete_id
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
