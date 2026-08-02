from api.services.ai_coach_production_cutover_service import (
    activate_production_chat_route,
    activate_production_conversation_route,
    verify_production_pipeline,
)


def test_activate_production_conversation_route():

    result = activate_production_conversation_route(
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


def test_activate_production_chat_route():

    result = activate_production_chat_route(
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


def test_verify_production_pipeline():

    result = verify_production_pipeline(
        {
            "success": True,
            "data": {
                "learning_applied": True,
            },
        },
    )

    assert result["production_ready"] is True
