from api.services.ai_coach_route_simplification_service import (
    simplify_chat_route,
    simplify_conversation_route,
    verify_route_architecture,
)


def test_simplify_conversation_route():

    result = simplify_conversation_route(
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


def test_simplify_chat_route():

    result = simplify_chat_route(
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


def test_verify_route_architecture():

    result = verify_route_architecture(
        {
            "success": True,
            "data": {
                "learning_applied": True,
            },
        },
    )

    assert result["architecture_valid"] is True
