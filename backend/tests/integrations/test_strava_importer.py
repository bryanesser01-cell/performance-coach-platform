from uuid import uuid4

from domain.activity.enums import (
    ActivityCategory,
    ActivitySource,
)
from integrations.strava import StravaActivityImporter


def test_strava_importer_creates_activity():
    athlete_id = uuid4()

    importer = StravaActivityImporter()

    activity = importer.import_activity(
        {
            "activity_id": "strava-456",
            "athlete_id": athlete_id,
            "activity_name": "Tempo Run",
            "start_time": "2026-07-28T06:00:00+00:00",
            "end_time": "2026-07-28T06:40:00+00:00",
            "distance": 8000,
            "duration": 2400,
            "average_hr": 150,
            "max_hr": 170,
            "cadence": 176,
            "elevation_gain": 65,
        }
    )

    assert activity.name == "Tempo Run"
    assert activity.category == ActivityCategory.RUNNING
    assert activity.source == ActivitySource.STRAVA
    assert activity.external_id == "strava-456"
    assert activity.athlete_id == athlete_id
