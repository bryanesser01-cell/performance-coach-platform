from datetime import date
from unittest.mock import Mock
from uuid import uuid4

import pytest

from application.services.athlete_service import AthleteService
from domain.athlete.entities import Athlete
from domain.athlete.exceptions import AthleteNotFound
from domain.athlete.repository import AthleteRepository


@pytest.fixture
def athlete():
    return Athlete.create(
        first_name="Bryan",
        last_name="Esser",
        date_of_birth=date(1981, 1, 1),
        sport="Running",
        height_cm=182,
        weight_kg=90.0,
    )


@pytest.fixture
def repository():
    return Mock(spec=AthleteRepository)


@pytest.fixture
def service(repository):
    return AthleteService(repository)


def test_get_athlete_returns_athlete(service, repository, athlete):
    # Arrange
    repository.get_by_id.return_value = athlete

    # Act
    result = service.get_athlete(athlete.id)

    # Assert
    assert result == athlete
    repository.get_by_id.assert_called_once_with(athlete.id)


def test_get_athlete_raises_not_found_when_missing(service, repository):
    # Arrange
    athlete_id = uuid4()
    repository.get_by_id.return_value = None

    # Act / Assert
    with pytest.raises(AthleteNotFound) as exc:
        service.get_athlete(athlete_id)

    assert str(exc.value) == f"Athlete with ID '{athlete_id}' was not found."
    repository.get_by_id.assert_called_once_with(athlete_id)


def test_create_athlete_returns_saved_athlete(service, repository, athlete):
    # Arrange
    repository.save.return_value = athlete

    # Act
    result = service.create_athlete(athlete)

    # Assert
    assert result == athlete
    repository.save.assert_called_once_with(athlete)


def test_update_athlete_returns_updated_athlete(service, repository, athlete):
    # Arrange
    repository.update.return_value = athlete

    # Act
    result = service.update_athlete(athlete)

    # Assert
    assert result == athlete
    repository.update.assert_called_once_with(athlete)


def test_delete_athlete_calls_repository(service, repository):
    # Arrange
    athlete_id = uuid4()

    # Act
    service.delete_athlete(athlete_id)

    # Assert
    repository.delete.assert_called_once_with(athlete_id)
