from unittest.mock import Mock, patch

from api.services.training_memory_service import (
    build_training_memory,
)


def test_training_memory_includes_workout_details():

    db = Mock()

    session = Mock()

    session.session_date = (
        "2026-08-01"
    )

    session.session_type = (
        "interval"
    )

    session.focus = (
        "5K speed"
    )

    session.status = (
        "completed"
    )

    session.intervals = [
        Mock(
            distance_meters=200,
            repetitions=4,
            target_time="40 seconds",
            recovery="60 seconds",
        ),
        Mock(
            distance_meters=1000,
            repetitions=1,
            target_time="3:45",
            recovery=None,
        ),
    ]

    with patch(
        "api.services.training_memory_service.TrainingSessionRepository",
    ) as repository:

        repository.return_value.get_recent_sessions.return_value = [
            session,
        ]

        result = build_training_memory(
            db=db,
            athlete_id=1,
        )

    workout = result[
        "training_history"
    ][0]["workout"]

    assert workout[0][
        "distance_meters"
    ] == 200

    assert workout[0][
        "repetitions"
    ] == 4


def test_training_memory_without_intervals():

    db = Mock()

    session = Mock()

    session.session_date = (
        "2026-08-01"
    )

    session.session_type = (
        "easy"
    )

    session.focus = (
        "recovery"
    )

    session.status = (
        "completed"
    )

    session.intervals = []

    with patch(
        "api.services.training_memory_service.TrainingSessionRepository",
    ) as repository:

        repository.return_value.get_recent_sessions.return_value = [
            session,
        ]

        result = build_training_memory(
            db=db,
            athlete_id=1,
        )

    assert (
        result["training_history"][0]["workout"]
        == []
    )
