from api.services.ai_coach_chat_service import (
    build_chat_context,
    execute_ai_coach_chat,
    format_chat_response,
)


def test_build_chat_context():

    result = build_chat_context(
        athlete_id=1,
        question="Should I train today?",
        athlete_profile={
            "sport": "running",
        },
        training_history=[],
        recovery_history=[],
        decision_analysis={},
        current_state={},
    )

    assert (
        result["athlete_id"]
        == 1
    )

    assert (
        result["question"]
        == "Should I train today?"
    )


def test_execute_ai_coach_chat():

    result = execute_ai_coach_chat(
        context={
            "athlete_id": 1,
            "question": "Should I recover?",
            "athlete_profile": {},
            "training_history": [],
            "recovery_history": [],
            "decision_analysis": {},
            "current_state": {},
        },
        ai_response={
            "coach_message": (
                "Recover today."
            ),
            "decision": (
                "REDUCE_TRAINING"
            ),
            "confidence": 90,
        },
    )

    assert (
        result["success"]
        is True
    )

    assert (
        result["athlete_id"]
        == 1
    )


def test_format_chat_response():

    result = format_chat_response(
        athlete_id=1,
        question="Should I run?",
        ai_response={
            "coach_message": (
                "Easy run today."
            ),
            "confidence": 85,
            "memory_used": True,
        },
        athlete_profile={
            "sport": "running",
        },
        training_history=[],
        recovery_history=[],
        decision_analysis={},
        current_state={},
    )

    assert (
        result["success"]
        is True
    )

    assert (
        result["memory_used"]
        is True
    )
