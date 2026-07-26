from datetime import date
from uuid import UUID

import pytest

from domain.training.entities import TrainingSession


def test_create_training_session():
    session = TrainingSession.create(
        athlete_id=UUID("12345678-1234-5678-1234-567812345678"),
        session_date=date(2026, 8, 1),
        session_type="Easy Run",
        duration_minutes=45,
        distance_km=8.5,
    )

    assert session.session_type == "Easy Run"
    assert session.duration_minutes == 45
    assert session.distance_km == 8.5


def test_create_training_session_with_invalid_duration():
    with pytest.raises(
        ValueError,
        match="Duration must be greater than 0.",
    ):
        TrainingSession.create(
            athlete_id=UUID("12345678-1234-5678-1234-567812345678"),
            session_date=date(2026, 8, 1),
            session_type="Easy Run",
            duration_minutes=0,
            distance_km=8.5,
        )


def test_training_session_calculates_pace():
    session = TrainingSession.create(
        athlete_id=UUID("12345678-1234-5678-1234-567812345678"),
        session_date=date(2026, 8, 1),
        session_type="Easy Run",
        duration_minutes=45,
        distance_km=9.0,
    )

    assert session.pace_minutes_per_km == 5.0
