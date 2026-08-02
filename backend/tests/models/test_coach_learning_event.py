from datetime import datetime

from database.models import (
    CoachLearningEvent,
)


def test_coach_learning_event_creation():

    event = CoachLearningEvent(
        athlete_id=1,
        decision="REDUCE_TRAINING",
        outcome="positive",
        confidence_change=5,
    )

    assert event.athlete_id == 1

    assert event.decision == "REDUCE_TRAINING"

    assert event.outcome == "positive"

    assert event.confidence_change == 5


def test_coach_learning_event_timestamp_field_exists():

    event = CoachLearningEvent(
        athlete_id=1,
        decision="PROGRESS_TRAINING",
        outcome="positive",
        confidence_change=2,
    )

    assert hasattr(
        event,
        "timestamp",
    )

    assert event.timestamp is None or isinstance(
        event.timestamp,
        datetime,
    )
