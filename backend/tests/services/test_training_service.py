from datetime import date
from unittest.mock import Mock
from uuid import UUID

from application.services.training_service import TrainingService
from domain.training.entities import TrainingSession


def test_create_training_session():
    repository = Mock()

    service = TrainingService(repository)

    session = TrainingSession.create(
        athlete_id=UUID("12345678-1234-5678-1234-567812345678"),
        session_date=date(2026, 8, 1),
        session_type="Easy Run",
        duration_minutes=45,
        distance_km=9.0,
    )

    service.create_training_session(session)

    repository.save.assert_called_once_with(session)
