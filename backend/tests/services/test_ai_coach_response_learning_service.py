from api.services.ai_coach_response_learning_service import (
    apply_learning_to_response,
    enrich_response_with_learning,
    finalise_ai_coach_response,
)


def test_apply_learning_to_response():

    result = apply_learning_to_response(
        athlete_id=1,
        question="Should I train today?",
        response={
            "decision": "REDUCE_TRAINING",
            "confidence": 90,
            "outcome": "positive",
        },
    )

    assert (
        result["learning_signal"]["signal"]
        == "REINFORCE"
    )


def test_enrich_response_with_learning():

    result = enrich_response_with_learning(
        response={
            "coach_message": (
                "Recover today."
            ),
        },
        learning_result={
            "signal": "REINFORCE",
        },
    )

    assert (
        result["learning_updated"]
        is True
    )

    assert (
        result["learning_result"]["signal"]
        == "REINFORCE"
    )


def test_finalise_ai_coach_response():

    result = finalise_ai_coach_response(
        athlete_id=1,
        question="Should I reduce training?",
        response={
            "decision": "REDUCE_TRAINING",
            "confidence": 85,
            "outcome": "positive",
        },
    )

    assert (
        result["learning_updated"]
        is True
    )

    assert (
        result["learning_result"]
        is not None
    )
