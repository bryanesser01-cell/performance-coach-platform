from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db

from api.services.training_database_service import (
    get_training_sessions_by_athlete,
)

from api.services.coach_engine import (
    generate_coach_response,
)

from schemas.coach import CoachResponse

router = APIRouter(
    prefix="/coach",
    tags=["Coach"],
)


@router.get(
    "/{athlete_id}",
    response_model=CoachResponse,
)
def get_coach_response(
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

    return generate_coach_response(
        sessions
    )