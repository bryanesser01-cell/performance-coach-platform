from unittest.mock import Mock, patch

from api.services.voice_memory_context_service import (
    build_voice_memory_context,
    generate_voice_memory_summary,
)


def test_build_voice_memory_context():

    db = Mock()

    mock_message = Mock()

    mock_message.user_message = "Should I train today?"

    mock_message.coach_response = "Your readiness looks good."

    with patch(
        "api.services.voice_memory_context_service.VoiceSessionRepository",
    ) as repository:

        repository.return_value.get_session_history.return_value = [
            mock_message,
        ]

        result = build_voice_memory_context(
            db=db,
            athlete_id=1,
            session_id="session-001",
        )

    assert result["has_history"] is True

    assert result["conversation_history"][0]["athlete"] == "Should I train today?"


def test_empty_voice_memory_context():

    db = Mock()

    with patch(
        "api.services.voice_memory_context_service.VoiceSessionRepository",
    ) as repository:

        repository.return_value.get_session_history.return_value = []

        result = build_voice_memory_context(
            db=db,
            athlete_id=1,
            session_id="session-001",
        )

    assert result["has_history"] is False


def test_generate_voice_memory_summary():

    context = {
        "has_history": True,
        "conversation_history": [
            {
                "athlete": "Question",
                "coach": "Answer",
            },
        ],
    }

    summary = generate_voice_memory_summary(
        context,
    )

    assert "1 previous" in summary
