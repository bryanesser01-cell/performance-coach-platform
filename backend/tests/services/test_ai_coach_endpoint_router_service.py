from api.services.ai_coach_endpoint_router_service import (
    normalise_endpoint_response,
    route_chat_request,
    route_conversation_request,
)


def test_route_conversation_request():

    result = route_conversation_request(
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


def test_route_chat_request():

    result = route_chat_request(
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


def test_normalise_endpoint_response():

    result = normalise_endpoint_response(
        {
            "success": True,
            "data": {
                "learning_applied": True,
            },
            "extra": "removed",
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
