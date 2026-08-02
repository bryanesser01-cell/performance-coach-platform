from api.services.ai_coach_endpoint_cutover_service import (
    cutover_chat_endpoint,
    cutover_conversation_endpoint,
    verify_endpoint_contract,
)


def test_cutover_conversation_endpoint():

    result = cutover_conversation_endpoint(
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


def test_cutover_chat_endpoint():

    result = cutover_chat_endpoint(
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


def test_verify_endpoint_contract():

    result = verify_endpoint_contract(
        {
            "success": True,
            "data": {
                "learning_applied": True,
            },
        },
    )

    assert result["valid"] is True
