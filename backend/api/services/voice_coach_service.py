from sqlalchemy.orm import Session

from api.services.ai_coach_conversation_service import (
    generate_coach_conversation_response,
)


def process_voice_coach_request(
    db: Session,
    athlete_id: int,
    voice_text: str,
) -> dict:
    """
    Process voice conversation.

    Current version:
    - Receives speech-to-text output
    - Sends to AI Coach conversation engine

    Future:
    - Speech recognition
    - Voice memory
    - Text-to-speech
    """

    coach_response = generate_coach_conversation_response(
        db=db,
        athlete_id=athlete_id,
        question=voice_text,
    )

    return {
        "athlete_id": athlete_id,
        "voice_input": voice_text,
        "response_text": coach_response["answer"],
        "decision": coach_response.get(
            "coach_decision",
        ),
    }
