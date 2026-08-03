from unittest.mock import Mock
from uuid import uuid4

from api.services.garmin_import_service import GarminImportService
from domain.activity.entities import Activity
from domain.activity.enums import (
    ActivityCategory,
    ActivitySource,
)


def build_activity() -> Activity:
    """
    Build a domain activity for testing.
    """

    return Activity(
        athlete_id=uuid4(),
        external_id="garmin-123",
        source=ActivitySource.GARMIN,
        category=ActivityCategory.RUNNING,
        name="Morning Run",
        started_at=None,
        ended_at=None,
    )


def test_imports_new_activity():

    activity = build_activity()

    repository = Mock()
    repository.exists.return_value = False

    importer = Mock()
    importer.get_activities.return_value = [
        activity,
    ]

    service = GarminImportService(
        repository,
        importer,
    )

    imported = service.import_activities(
        activity.athlete_id,
    )

    repository.create.assert_called_once_with(
        activity,
    )

    assert (
        len(
            imported,
        )
        == 1
    )

    assert imported[0] == activity


def test_skips_duplicate_activity():

    activity = build_activity()

    repository = Mock()
    repository.exists.return_value = True

    importer = Mock()
    importer.get_activities.return_value = [
        activity,
    ]

    service = GarminImportService(
        repository,
        importer,
    )

    imported = service.import_activities(
        activity.athlete_id,
    )

    repository.create.assert_not_called()

    assert imported == []


def test_imports_multiple_activities():

    activity_one = build_activity()

    activity_two = Activity(
        athlete_id=activity_one.athlete_id,
        external_id="garmin-456",
        source=ActivitySource.GARMIN,
        category=ActivityCategory.RUNNING,
        name="Evening Run",
        started_at=None,
        ended_at=None,
    )

    repository = Mock()
    repository.exists.return_value = False

    importer = Mock()
    importer.get_activities.return_value = [
        activity_one,
        activity_two,
    ]

    service = GarminImportService(
        repository,
        importer,
    )

    imported = service.import_activities(
        activity_one.athlete_id,
    )

    assert (
        len(
            imported,
        )
        == 2
    )

    assert repository.create.call_count == 2
