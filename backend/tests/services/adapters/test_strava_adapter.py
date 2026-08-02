from api.services.adapters.strava_adapter import (
    build_strava_training_record,
    convert_strava_activity,
)


def test_convert_strava_activity():

    result = convert_strava_activity(
        {
            "activity_id": 789,
            "date": "2026-07-30",
            "distance_meters": 5000,
            "moving_time_seconds": 1500,
            "average_heartrate": 145,
            "max_heartrate": 165,
            "cadence": 172,
        }
    )

    assert result["source"] == "strava"

    assert result["distance_km"] == 5

    assert result["pace"] == "5:00/km"


def test_strava_import_pipeline():

    result = build_strava_training_record(
        {
            "distance_meters": 5000,
            "moving_time_seconds": 1500,
        }
    )

    assert result["import_complete"] is True
