from fastapi import HTTPException
from sqlalchemy.orm import Session

from repositories.training_repository import TrainingRepository

from api.services.coach_engine import (
    generate_coach_response,
)


def get_coach_response_service(
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

    return generate_coach_response(sessions)
