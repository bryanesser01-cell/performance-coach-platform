from sqlalchemy.orm import Session

from database.repositories.voice_session_repository import (
    VoiceSessionRepository,
)


def build_voice_memory_context(
    db: Session,
    athlete_id: int,
    session_id: str,
) -> dict:
    """
    Build previous voice conversation context.

    Uses:
    - Previous athlete questions
    - Previous coach responses

    Used by AI Coach to maintain continuity.
    """

    repository = VoiceSessionRepository(
        db,
    )

    history = repository.get_session_history(
        athlete_id=athlete_id,
        session_id=session_id,
    )

    conversations = []

    for message in history:

        conversations.append(
            {
                "athlete": (message.user_message),
                "coach": (message.coach_response),
            }
        )

    return {
        "athlete_id": athlete_id,
        "session_id": session_id,
        "conversation_history": conversations,
        "has_history": len(
            conversations,
        )
        > 0,
    }


def generate_voice_memory_summary(
    context: dict,
) -> str:
    """
    Generate summary of previous
    voice conversations.
    """

    if not context.get(
        "has_history",
        False,
    ):
        return "No previous voice conversation " "history available."

    count = len(context["conversation_history"])

    return (
        f"The athlete has had "
        f"{count} previous coaching "
        f"conversation(s) in this session."
    )
