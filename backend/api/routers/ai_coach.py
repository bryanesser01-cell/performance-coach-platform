from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.services.ai_coach_engine_service import (
    generate_ai_coach_response,
)
from api.services.ai_coach_orchestrator_service import (
    run_ai_coach_orchestrator,
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
    Generate complete AI Coach response.

    Legacy AI Coach engine endpoint.
    """

    return generate_ai_coach_response(
        db,
        athlete_id,
    )


@router.get("/{athlete_id}/coach")
def get_ai_coach_orchestrated_response(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    """
    Generate AI Coach adaptive recommendation.

    Flow:

    Athlete State
        ↓
    AI Coach Orchestrator
        ↓
    Adaptive Decision
        ↓
    Coaching Recommendation
    """

    return run_ai_coach_orchestrator(
        db=db,
        athlete_id=athlete_id,
    )
