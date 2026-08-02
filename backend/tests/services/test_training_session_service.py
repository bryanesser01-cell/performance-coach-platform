from datetime import datetime
from unittest.mock import Mock

from api.services.training_session_service import (
    analyse_completed_session,
    complete_training_session,
    create_training_session,
    get_upcoming_sessions,
)
from database.training_models import TrainingSession


def test_create_training_session():

    db = Mock()

    session = TrainingSession(
        id=1,
        athlete_id=1,
        session_date=datetime(
            2026,
            7,
            30,
        ),
        session_type="interval",
        focus="Speed",
        status="planned",
    )

    db.refresh.side_effect = lambda obj: None

    result = create_training_session(
        db=db,
        athlete_id=1,
        session_date=session.session_date,
        session_type="interval",
        focus="Speed",
    )

    assert result["athlete_id"] == 1

    assert result["session_type"] == "interval"


def test_complete_training_session():

    db = Mock()

    session = TrainingSession(
        id=1,
        athlete_id=1,
        session_date=datetime(
            2026,
            7,
            30,
        ),
        session_type="tempo",
        focus="Threshold",
        status="planned",
    )

    db.query.return_value.filter.return_value.first.return_value = session

    result = complete_training_session(
        db=db,
        session_id=1,
        notes="Felt strong",
    )

    assert result["status"] == "completed"

    assert result["notes"] == "Felt strong"


def test_get_upcoming_sessions():

    db = Mock()

    db.query.return_value.filter.return_value.order_by.return_value.all.return_value = [
        "session1",
        "session2",
    ]

    result = get_upcoming_sessions(
        db=db,
        athlete_id=1,
    )

    assert len(result) == 2


def test_analyse_completed_session():

    session = TrainingSession(
        id=1,
        athlete_id=1,
        session_date=datetime(
            2026,
            7,
            30,
        ),
        session_type="long_run",
        focus="Endurance",
        status="completed",
    )

    result = analyse_completed_session(
        session,
    )

    assert result["status"] == "completed"

    assert "recovery" in result["recommendation"]
