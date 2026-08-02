from api.services.ai_coach_response_pipeline_service import (
    apply_response_learning,
    finalise_live_response,
    run_coach_response_pipeline,
)


def test_run_coach_response_pipeline():

    result = run_coach_response_pipeline(
        athlete_id=1,
        question="Should I train today?",
        response={
            "decision": "REDUCE_TRAINING",
            "confidence": 90,
            "outcome": "positive",
        },
    )

    assert result["learning_applied"] is True


def test_apply_response_learning():

    result = apply_response_learning(
        response={
            "coach_message": ("Recover today."),
        },
        learning_response={
            "learning_context": {
                "learning_updated": True,
            },
        },
    )

    assert result["learning_applied"] is True

    assert result["learning_context"]["learning_updated"] is True


def test_finalise_live_response():

    result = finalise_live_response(
        athlete_id=1,
        question="Should I reduce training?",
        response={
            "decision": "REDUCE_TRAINING",
            "confidence": 85,
            "outcome": "positive",
        },
    )

    assert result["learning_applied"] is True

    assert result["learning_context"] is not None
