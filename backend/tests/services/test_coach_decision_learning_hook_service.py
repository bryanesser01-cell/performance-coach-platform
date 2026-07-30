from unittest.mock import Mock, patch

from api.services.coach_decision_learning_hook_service import (
    create_learning_hook_result,
    prepare_learning_hook,
    process_coach_outcome,
    update_decision_confidence,
)


def test_prepare_learning_hook():

    result = prepare_learning_hook(
        decision="REDUCE_TRAINING",
        athlete_id=1,
    )

    assert (
        result["decision"]
        == "REDUCE_TRAINING"
    )

    assert (
        result["status"]
        == "awaiting_outcome"
    )


def test_process_coach_outcome():

    db = Mock()

    with patch(
        "api.services.coach_decision_learning_hook_service.capture_coach_decision_outcome",
        return_value={
            "confidence_change": 10,
        },
    ):

        result = process_coach_outcome(
            db=db,
            athlete_id=1,
            decision="REDUCE_TRAINING",
            outcome="positive",
        )

    assert (
        result["outcome"]
        == "positive"
    )


def test_update_decision_confidence():

    result = update_decision_confidence(
        {
            "confidence": 70,
        },
        {
            "confidence_change": 10,
        },
    )

    assert (
        result["confidence"]
        == 80
    )


def test_create_learning_hook_result():

    result = create_learning_hook_result(
        decision="PROGRESS_TRAINING",
        athlete_id=1,
        confidence=75,
    )

    assert (
        result["confidence"]
        == 75
    )

    assert (
        result["learning_status"]
        == "active"
    )
