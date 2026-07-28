from datetime import UTC, datetime
from unittest.mock import Mock, patch
from uuid import uuid4

from api.services.activity_ingestion_service import (
    ingest_activity,
)
from domain.activity.entities import Activity
from domain.activity.enums import (
    ActivityCategory,
    ActivitySource,
)


def test_ingest_activity_creates_activity():
    db = Mock()

    athlete_id = uuid4()

    importer = Mock()

    importer.import_activity.return_value = Activity(
        athlete_id=athlete_id,
        category=ActivityCategory.RUNNING,
        name="Morning Run",
        started_at=datetime.now(UTC),
        source=ActivitySource.GARMIN,
        external_id="garmin-123",
    )

    mock_repository = Mock()

    saved_activity = Mock()

    mock_repository.get_by_external_id.return_value = None

    mock_repository.create.return_value = saved_activity

    with patch(
        "api.services.activity_ingestion_service.ActivityRepository",
        return_value=mock_repository,
    ):
        result = ingest_activity(
            db,
            importer,
            {
                "activity_id": "garmin-123",
            },
        )

    assert result == saved_activity

    mock_repository.create.assert_called_once()


def test_ingest_activity_returns_existing_activity():
    db = Mock()

    importer = Mock()

    existing_activity = Mock()

    mock_repository = Mock()

    mock_repository.get_by_external_id.return_value = (
        existing_activity
    )

    with patch(
        "api.services.activity_ingestion_service.ActivityRepository",
        return_value=mock_repository,
    ):
        result = ingest_activity(
            db,
            importer,
            {
                "activity_id": "garmin-123",
            },
        )

    assert result == existing_activity

    importer.import_activity.assert_not_called()
