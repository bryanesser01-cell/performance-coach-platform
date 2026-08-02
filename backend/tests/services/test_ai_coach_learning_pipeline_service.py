from api.services.ai_coach_learning_pipeline_service import (
    build_learning_enriched_response,
    process_completed_coaching_event,
    run_learning_pipeline,
    trigger_learning_from_response,
)


def test_trigger_learning_from_response():

    result = trigger_learning_from_response(
        athlete_id=1,
        question="Should I train today?",
        response={
            "decision": "REDUCE_TRAINING",
            "confidence": 90,
            "outcome": "positive",
        },
    )

    assert result["learning_signal"]["signal"] == "REINFORCE"


def test_process_completed_coaching_event():

    result = process_completed_coaching_event(
        athlete_id=1,
        question="Recover?",
        response={
            "decision": "REDUCE_TRAINING",
            "confidence": 85,
            "outcome": "positive",
        },
    )

    assert result["athlete_id"] == 1

    assert result["learning_result"] is not None


def test_build_learning_enriched_response():

    result = build_learning_enriched_response(
        response={
            "coach_message": ("Recover today."),
        },
        learning_result={
            "learning_updated": True,
        },
    )

    assert result["learning_updated"] is True


def test_run_learning_pipeline():

    result = run_learning_pipeline(
        athlete_id=1,
        question="Should I reduce training?",
        response={
            "decision": "REDUCE_TRAINING",
            "confidence": 90,
            "outcome": "positive",
        },
    )

    assert result["learning_updated"] is True

    assert result["learning_result"] is not None
