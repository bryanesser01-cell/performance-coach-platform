from api.services.ai_coach_route_cutover_service import (
    execute_chat_cutover,
    execute_conversation_cutover,
    verify_cutover_response,
)


def test_execute_conversation_cutover():

    result = execute_conversation_cutover(
        athlete_id=1,
        question="Should I train today?",
        response={
            "decision": "REDUCE_TRAINING",
            "confidence": 90,
            "outcome": "positive",
        },
    )

    assert (
        result["success"]
        is True
    )

    assert (
        result["data"]["learning_applied"]
        is True
    )


def test_execute_chat_cutover():

    result = execute_chat_cutover(
        athlete_id=1,
        question="Should I recover?",
        response={
            "decision": "RECOVERY",
            "confidence": 85,
            "outcome": "positive",
        },
    )

    assert (
        result["success"]
        is True
    )

    assert (
        result["data"]["learning_applied"]
        is True
    )


def test_verify_cutover_response():

    result = verify_cutover_response(
        {
            "success": True,
            "data": {
                "learning_applied": True,
            },
        },
    )

    assert (
        result["cutover_successful"]
        is True
    )
