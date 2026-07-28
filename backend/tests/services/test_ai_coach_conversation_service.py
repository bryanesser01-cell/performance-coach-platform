from unittest.mock import Mock, patch

from api.services.ai_coach_conversation_service import (
    generate_coach_conversation_response,
)


def test_training_question_returns_training_advice():

    db = Mock()

    with patch(
        "api.services.ai_coach_conversation_service.generate_ai_coach_response",
        return_value={
            "coach_message": "Keep progressing.",
            "recommendation": "Continue training.",
        },
    ):

        result = generate_coach_conversation_response(
            db,
            athlete_id=1,
            question="Should I train today?",
        )

    assert (
        result["athlete_id"]
        == 1
    )

    assert (
        "training"
        in result["answer"]
    )


def test_recovery_question_returns_recovery_advice():

    db = Mock()

    with patch(
        "api.services.ai_coach_conversation_service.generate_ai_coach_response",
        return_value={},
    ):

        result = generate_coach_conversation_response(
            db,
            athlete_id=1,
            question="Do I need recovery?",
        )

    assert (
        "Recovery"
        in result["answer"]
    )


def test_race_question_returns_race_advice():

    db = Mock()

    with patch(
        "api.services.ai_coach_conversation_service.generate_ai_coach_response",
        return_value={},
    ):

        result = generate_coach_conversation_response(
            db,
            athlete_id=1,
            question="How should I prepare for my race?",
        )

    assert (
        "race"
        in result["answer"]
    )


def test_ai_coach_conversation_uses_memory_context():

    db = Mock()

    with patch(
        "api.services.ai_coach_conversation_service.enrich_coach_prompt",
        return_value={
            "athlete_id": 1,
            "question": "Should I train today?",
            "memory_context": {
                "goal": [
                    "Run sub 20 minute 5K",
                ],
                "preference": [
                    "Prefers morning sessions",
                ],
            },
        },
    ), patch(
        "api.services.ai_coach_conversation_service.generate_ai_coach_response",
        return_value={
            "coach_message": "Keep progressing.",
            "recommendation": "Continue training.",
        },
    ):

        result = generate_coach_conversation_response(
            db=db,
            athlete_id=1,
            question="Should I train today?",
        )

    assert (
        result["memory_context"]["goal"][0]
        == "Run sub 20 minute 5K"
    )

    assert (
        result["memory_context"]["preference"][0]
        == "Prefers morning sessions"
    )

    assert (
        result["answer"]
        == "Your training should follow your current "
        "fitness trend, recovery status, and goals."
    )
