from api.services.ai_coach_core_service import (
    process_ai_coach_chat,
    process_ai_coach_conversation,
    process_ai_coach_request,
)


def test_process_ai_coach_request():

    result = process_ai_coach_request(
        athlete_id=1,
        question="Should I train today?",
        response={
            "decision": "REDUCE_TRAINING",
            "confidence": 90,
            "outcome": "positive",
        },
    )

    assert result["success"] is True

    assert result["data"]["learning_applied"] is True


def test_process_ai_coach_conversation():

    result = process_ai_coach_conversation(
        athlete_id=1,
        question="Should I recover?",
        response={
            "decision": "RECOVERY",
            "confidence": 85,
            "outcome": "positive",
        },
    )

    assert result["success"] is True


def test_process_ai_coach_chat():

    result = process_ai_coach_chat(
        athlete_id=1,
        question="What should I run today?",
        response={
            "decision": "EASY_RUN",
            "confidence": 80,
            "outcome": "positive",
        },
    )

    assert result["success"] is True

    assert result["data"]["learning_applied"] is True
