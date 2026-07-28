from uuid import uuid4

from domain.activity.enums import (
    ActivityCategory,
    ActivitySource,
)
from integrations.garmin import GarminActivityImporter


def test_garmin_importer_creates_activity():
    athlete_id = uuid4()

    importer = GarminActivityImporter()

    activity = importer.import_activity(
        {
            "activity_id": "garmin-123",
            "athlete_id": athlete_id,
            "activity_name": "Morning Run",
            "start_time": "2026-07-28T06:00:00+00:00",
            "end_time": "2026-07-28T06:30:00+00:00",
            "distance": 5000,
            "duration": 1800,
            "average_hr": 145,
            "max_hr": 165,
            "cadence": 172,
            "elevation_gain": 50,
        }
    )

    assert activity.name == "Morning Run"
    assert activity.category == ActivityCategory.RUNNING
    assert activity.source == ActivitySource.GARMIN
    assert activity.external_id == "garmin-123"
    assert activity.athlete_id == athlete_id
