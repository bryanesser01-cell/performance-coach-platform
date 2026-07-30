from api.services.ai_coach_live_learning_service import (
    apply_live_learning,
    build_final_coach_output,
    process_live_coach_response,
)


def test_process_live_coach_response():

    result = process_live_coach_response(
        athlete_id=1,
        question="Should I train today?",
        response={
            "decision": "REDUCE_TRAINING",
            "confidence": 90,
            "outcome": "positive",
        },
    )

    assert (
        result["learning_context"]
        is not None
    )


def test_apply_live_learning():

    result = apply_live_learning(
        response={
            "coach_message": (
                "Recover today."
            ),
        },
        learning_response={
            "learning_context": {
                "learning_updated": True,
            },
        },
    )

    assert (
        result["learning_applied"]
        is True
    )

    assert (
        result["learning_context"]
        ["learning_updated"]
        is True
    )


def test_build_final_coach_output():

    result = build_final_coach_output(
        athlete_id=1,
        question="Should I reduce training?",
        response={
            "decision": "REDUCE_TRAINING",
            "confidence": 85,
            "outcome": "positive",
        },
    )

    assert (
        result["learning_applied"]
        is True
    )

    assert (
        result["learning_context"]
        is not None
    )
