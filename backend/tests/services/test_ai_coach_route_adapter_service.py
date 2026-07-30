from api.services.ai_coach_route_adapter_service import (
    adapt_chat_route,
    adapt_conversation_route,
    prepare_route_context,
)


def test_prepare_route_context():

    result = prepare_route_context(
        athlete_id=1,
        question="Should I train today?",
        response={
            "decision": "REDUCE_TRAINING",
        },
    )

    assert (
        result["athlete_id"]
        == 1
    )

    assert (
        result["question"]
        == "Should I train today?"
    )


def test_adapt_conversation_route():

    result = adapt_conversation_route(
        athlete_id=1,
        question="Should I recover?",
        response={
            "decision": "RECOVERY",
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


def test_adapt_chat_route():

    result = adapt_chat_route(
        athlete_id=1,
        question="Should I run today?",
        response={
            "decision": "EASY_RUN",
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
