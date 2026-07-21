from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db

from api.services.coach_service import (
    get_coach_response_service,
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
    return get_coach_response_service(
        db,
        athlete_id,
    )