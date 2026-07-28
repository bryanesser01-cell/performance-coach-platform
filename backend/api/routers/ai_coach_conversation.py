from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.services.ai_coach_conversation_service import (
    generate_coach_conversation_response,
)
from database.session import get_db

router = APIRouter(
    prefix="/athletes",
    tags=["AI Coach Conversation"],
)


@router.post("/{athlete_id}/ai-coach/chat")
def ask_ai_coach(
    athlete_id: int,
    question: str,
    db: Session = Depends(get_db),
):
    """
    Ask AI coach a question.
    """

    return generate_coach_conversation_response(
        db,
        athlete_id,
        question,
    )
