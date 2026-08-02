from api.services.ai_coach_response_formatter_service import (
    build_standard_coach_response,
    format_ai_coach_response,
    validate_coach_response,
)


def test_format_ai_coach_response():

    result = format_ai_coach_response(
        athlete_id=1,
        question="Should I train today?",
        coach_response={
            "coach_message": ("Recover today."),
            "decision": ("REDUCE_TRAINING"),
            "recommendation": ("Easy recovery run."),
            "confidence": 90,
            "memory_used": True,
            "learning_updated": True,
            "strategy": ("RECOVERY_FIRST"),
        },
    )

    assert result["athlete_id"] == 1

    assert result["decision"] == "REDUCE_TRAINING"

    assert result["confidence"] == 90


def test_build_standard_response():

    result = build_standard_coach_response(
        athlete_id=1,
        question="Should I run?",
        message="Run easy today.",
        decision="MAINTAIN_TRAINING",
        recommendation="Easy aerobic run.",
        confidence=85,
        memory_used=True,
        learning_updated=True,
        strategy="EASY_DAY",
    )

    assert result["success"] is True

    assert result["strategy"] == "EASY_DAY"

    assert result["memory_used"] is True


def test_validate_response():

    result = validate_coach_response(
        {
            "success": True,
            "athlete_id": 1,
            "coach_message": ("Recovery recommended."),
            "confidence": 80,
        }
    )

    assert result is True
