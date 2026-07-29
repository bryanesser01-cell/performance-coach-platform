from unittest.mock import Mock, patch

from api.services.voice_coach_service import (
    process_voice_coach_request,
)


def test_voice_coach_processes_text():

    db = Mock()

    with patch(
        "api.services.voice_coach_service.generate_coach_conversation_response",
        return_value={
            "answer": "Your training looks good today.",
            "coach_decision": {
                "decision": "progress_training",
            },
        },
    ):

        result = process_voice_coach_request(
            db=db,
            athlete_id=1,
            voice_text="Should I train today?",
        )

    assert (
        result["athlete_id"]
        == 1
    )

    assert (
        result["voice_input"]
        == "Should I train today?"
    )

    assert (
        "training"
        in result["response_text"]
    )
