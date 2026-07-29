from unittest.mock import Mock, patch

from api.services.voice_session_service import (
    process_voice_session,
)


def test_voice_session_stores_conversation():

    db = Mock()

    with patch(
        "api.services.voice_session_service.process_voice_coach_request",
        return_value={
            "response_text": (
                "Your training looks good today."
            ),
            "decision": {
                "decision": (
                    "progress_training"
                ),
            },
        },
    ), patch(
        "api.services.voice_session_service.VoiceSessionRepository",
    ) as repository:

        result = process_voice_session(
            db=db,
            athlete_id=1,
            session_id="session-001",
            voice_text=(
                "Should I train today?"
            ),
        )

    repository.return_value.create_session_message.assert_called_once()

    assert (
        result["session_id"]
        == "session-001"
    )

    assert (
        result["athlete_id"]
        == 1
    )

    assert (
        "training"
        in result["answer"]
    )
