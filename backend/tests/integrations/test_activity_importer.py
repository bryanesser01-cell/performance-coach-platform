from datetime import UTC, datetime
from uuid import uuid4

from domain.activity.entities import Activity
from domain.activity.enums import (
    ActivityCategory,
    ActivitySource,
    ActivityStatus,
)
from integrations.base import ActivityImporter


class MockActivityImporter(ActivityImporter):
    """
    Test implementation of ActivityImporter.
    """

    def import_activity(
        self,
        payload: dict,
    ) -> Activity:
        return Activity(
            athlete_id=uuid4(),
            category=ActivityCategory.RUNNING,
            name=payload["name"],
            started_at=datetime.now(UTC),
            source=ActivitySource.GARMIN,
            external_id=payload.get("id"),
        )


def test_activity_importer_creates_activity():
    importer = MockActivityImporter()

    activity = importer.import_activity(
        {
            "id": "garmin-123",
            "name": "Morning Run",
        }
    )

    assert activity.name == "Morning Run"
    assert activity.category == ActivityCategory.RUNNING
    assert activity.source == ActivitySource.GARMIN
    assert activity.external_id == "garmin-123"
    assert activity.status == ActivityStatus.PLANNED
