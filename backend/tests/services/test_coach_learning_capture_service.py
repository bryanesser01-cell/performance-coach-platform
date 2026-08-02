from unittest.mock import Mock, patch

from api.services.coach_learning_capture_service import (
    calculate_learning_update,
    capture_coach_decision_outcome,
    store_learning_feedback,
)


def test_positive_learning_update():

    result = calculate_learning_update(
        "positive",
    )

    assert result == 10


def test_negative_learning_update():

    result = calculate_learning_update(
        "negative",
    )

    assert result == -10


def test_capture_decision_outcome():

    db = Mock()

    with patch(
        "api.services.coach_learning_capture_service.record_learning_event",
        return_value={
            "id": 1,
        },
    ):

        result = capture_coach_decision_outcome(
            db=db,
            athlete_id=1,
            decision="REDUCE_TRAINING",
            outcome="positive",
        )

    assert result["confidence_change"] == 10

    assert result["outcome"] == "positive"


def test_store_learning_feedback():

    db = Mock()

    with patch(
        "api.services.coach_learning_capture_service.record_learning_event",
        return_value={
            "id": 1,
        },
    ):

        result = store_learning_feedback(
            db=db,
            athlete_id=1,
            decision="PROGRESS_TRAINING",
            completed=True,
            performance_change="improved",
        )

    assert result["outcome"] == "positive"
