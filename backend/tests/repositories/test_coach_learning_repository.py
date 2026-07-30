from unittest.mock import Mock

from database.repositories.coach_learning_repository import (
    calculate_confidence_adjustment,
    create_learning_event,
    get_learning_history,
    get_recent_decisions,
)


class MockLearningEvent:
    def __init__(
        self,
        confidence_change: int,
    ):
        self.confidence_change = confidence_change


def test_create_learning_event():

    db = Mock()

    db.refresh.side_effect = (
        lambda event: None
    )

    result = create_learning_event(
        db=db,
        athlete_id=1,
        decision="REDUCE_TRAINING",
        outcome="positive",
        confidence_change=5,
    )

    assert (
        result.athlete_id
        == 1
    )

    assert (
        result.decision
        == "REDUCE_TRAINING"
    )

    assert (
        result.outcome
        == "positive"
    )

    assert (
        result.confidence_change
        == 5
    )

    db.add.assert_called_once()

    db.commit.assert_called_once()

    db.refresh.assert_called_once()


def test_get_learning_history():

    db = Mock()

    query = db.query.return_value

    (
        query.filter.return_value
        .order_by.return_value
        .limit.return_value
        .all.return_value
    ) = [
        "event_1",
        "event_2",
    ]

    result = get_learning_history(
        db=db,
        athlete_id=1,
    )

    assert result == [
        "event_1",
        "event_2",
    ]


def test_get_recent_decisions_with_filter():

    db = Mock()

    query = db.query.return_value

    (
        query.filter.return_value
        .filter.return_value
        .order_by.return_value
        .limit.return_value
        .all.return_value
    ) = [
        "decision_event",
    ]

    result = get_recent_decisions(
        db=db,
        athlete_id=1,
        decision="PROGRESS_TRAINING",
    )

    assert result == [
        "decision_event",
    ]


def test_calculate_confidence_adjustment():

    events = [
        MockLearningEvent(5),
        MockLearningEvent(3),
        MockLearningEvent(-2),
    ]

    result = calculate_confidence_adjustment(
        events,
    )

    assert result == 6


def test_calculate_confidence_adjustment_empty():

    result = calculate_confidence_adjustment(
        [],
    )

    assert result == 0
