from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.services.voice_coach_service import (
    process_voice_coach_request,
)
from database.session import get_db

router = APIRouter(
    prefix="/voice-coach",
    tags=["voice-coach"],
)


@router.post("/chat")
def voice_coach_chat(
    athlete_id: int,
    voice_text: str,
    db: Session = Depends(get_db),
):
    """
    Voice coach conversation endpoint.

    Input:
    Speech converted to text.

    Output:
    AI coach response.
    """

    return process_voice_coach_request(
        db=db,
        athlete_id=athlete_id,
        voice_text=voice_text,
    )
