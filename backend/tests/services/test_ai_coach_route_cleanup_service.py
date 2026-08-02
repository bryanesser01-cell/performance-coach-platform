from api.services.ai_coach_route_cleanup_service import (
    cleanup_chat_route,
    cleanup_conversation_route,
    verify_no_legacy_path,
)


def test_cleanup_conversation_route():

    result = cleanup_conversation_route(
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


def test_cleanup_chat_route():

    result = cleanup_chat_route(
        athlete_id=1,
        question="Should I recover?",
        response={
            "decision": "RECOVERY",
            "confidence": 85,
            "outcome": "positive",
        },
    )

    assert result["success"] is True

    assert result["data"]["learning_applied"] is True


def test_verify_no_legacy_path():

    result = verify_no_legacy_path(
        {
            "success": True,
            "data": {
                "learning_applied": True,
            },
        },
    )

    assert result["legacy_removed"] is True
