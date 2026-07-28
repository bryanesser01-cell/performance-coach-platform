from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.services.ai_coach_engine_service import (
    generate_ai_coach_response,
)
from database.session import get_db

router = APIRouter(
    prefix="/athletes",
    tags=["AI Coach"],
)


@router.get("/{athlete_id}/ai-coach")
def get_ai_coach_response(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    """
    Generate complete AI coach response.
    """

    return generate_ai_coach_response(
        db,
        athlete_id,
    )
