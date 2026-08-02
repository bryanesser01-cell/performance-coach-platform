from api.services.adapters.apple_health_adapter import (
    build_apple_health_record,
    convert_apple_health_workout,
)


def test_convert_apple_health_workout():

    result = convert_apple_health_workout(
        {
            "workout_id": 123,
            "date": "2026-07-30",
            "distance_km": 5,
            "duration_minutes": 25,
            "heart_rate": 145,
            "max_heart_rate": 165,
            "cadence": 172,
        }
    )

    assert result["source"] == "apple_health"

    assert result["distance_km"] == 5

    assert result["pace"] == "5:00/km"


def test_apple_health_import_pipeline():

    result = build_apple_health_record(
        {
            "distance_km": 5,
            "duration_minutes": 25,
        }
    )

    assert result["import_complete"] is True
