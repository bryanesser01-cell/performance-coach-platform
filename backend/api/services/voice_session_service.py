from sqlalchemy.orm import Session

from api.services.voice_coach_service import (
    process_voice_coach_request,
)
from database.repositories.voice_session_repository import (
    VoiceSessionRepository,
)


def process_voice_session(
    db: Session,
    athlete_id: int,
    session_id: str,
    voice_text: str,
) -> dict:
    """
    Process voice conversation
    and store session memory.
    """

    response = process_voice_coach_request(
        db=db,
        athlete_id=athlete_id,
        voice_text=voice_text,
    )

    repository = VoiceSessionRepository(
        db,
    )

    repository.create_session_message(
        athlete_id=athlete_id,
        session_id=session_id,
        user_message=voice_text,
        coach_response=response[
            "response_text"
        ],
    )

    return {
        "session_id": session_id,
        "athlete_id": athlete_id,
        "question": voice_text,
        "answer": response[
            "response_text"
        ],
        "decision": response.get(
            "decision",
        ),
    }


def get_voice_session_history(
    db: Session,
    athlete_id: int,
    session_id: str,
) -> list:
    """
    Retrieve previous voice conversation.
    """

    repository = VoiceSessionRepository(
        db,
    )

    return repository.get_session_history(
        athlete_id=athlete_id,
        session_id=session_id,
    )
