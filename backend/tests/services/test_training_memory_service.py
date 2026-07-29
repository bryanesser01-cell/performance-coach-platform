from unittest.mock import Mock, patch

from api.services.training_memory_service import (
    build_training_memory,
    generate_training_memory_summary,
)


def test_build_training_memory():

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
        result["has_training_history"]
        is True
    )

    assert (
        result["training_history"][0][
            "type"
        ]
        == "interval"
    )


def test_empty_training_memory():

    db = Mock()

    with patch(
        "api.services.training_memory_service.TrainingSessionRepository",
    ) as repository:

        repository.return_value.get_recent_sessions.return_value = []

        result = build_training_memory(
            db=db,
            athlete_id=1,
        )

    assert (
        result["has_training_history"]
        is False
    )


def test_training_memory_summary():

    summary = generate_training_memory_summary(
        {
            "has_training_history": True,
            "training_history": [
                {}
            ],
        }
    )

    assert (
        "1 recent"
        in summary
    )
