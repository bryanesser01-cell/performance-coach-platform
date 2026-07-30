from api.services.ai_coach_route_pipeline_service import (
    build_route_response,
    process_chat_request,
    process_conversation_request,
)


def test_process_conversation_request():

    result = process_conversation_request(
        athlete_id=1,
        question="Should I train today?",
        response={
            "decision": "REDUCE_TRAINING",
            "confidence": 90,
            "outcome": "positive",
        },
    )

    assert (
        result["learning_applied"]
        is True
    )


def test_process_chat_request():

    result = process_chat_request(
        athlete_id=1,
        question="Should I recover?",
        response={
            "decision": "RECOVERY",
            "confidence": 85,
            "outcome": "positive",
        },
    )

    assert (
        result["learning_applied"]
        is True
    )


def test_build_route_response():

    result = build_route_response(
        {
            "coach_message": (
                "Recover today."
            ),
        },
    )

    assert (
        result["success"]
        is True
    )

    assert (
        result["data"]["coach_message"]
        == "Recover today."
    )
