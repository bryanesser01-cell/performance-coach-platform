from fastapi import HTTPException
from sqlalchemy.orm import Session

from api.services.coach_engine import (
    generate_coach_response,
)
from api.services.coach_intelligence_service import (
    generate_coach_insights,
)
from database.repositories.training_repository import TrainingRepository


def get_coach_response_service(
    db: Session,
    athlete_id: int,
):
    """
    Generate complete coach response.

    Combines:
    - Coach engine output
    - Performance intelligence insights
    """

    training_repository = TrainingRepository(db)

    sessions = training_repository.get_by_athlete(
        athlete_id,
    )

    if not sessions:
        raise HTTPException(
            status_code=404,
            detail="No training sessions found.",
        )

    coach_response = generate_coach_response(
        sessions,
    )

    intelligence = generate_coach_insights(
        db,
        athlete_id,
    )

    return {
        "analysis": coach_response.analysis,
        "workout": coach_response.workout,
        "recommendations": coach_response.recommendations,
        "insights": intelligence,
    }
