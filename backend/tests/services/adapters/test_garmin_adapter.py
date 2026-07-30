from api.services.adapters.garmin_adapter import (
    build_garmin_training_record,
    convert_garmin_activity,
)


def test_convert_garmin_activity():

    result = convert_garmin_activity(
        {
            "activity_id": 123,
            "date": "2026-07-30",
            "distance_meters": 5000,
            "duration_seconds": 1500,
            "average_hr": 145,
            "max_hr": 165,
            "cadence": 172,
        }
    )


    assert (
        result["source"]
        == "garmin"
    )

    assert (
        result["distance_km"]
        == 5
    )

    assert (
        result["pace"]
        == "5:00/km"
    )



def test_garmin_import_pipeline():

    result = build_garmin_training_record(
        {
            "distance_meters": 5000,
            "duration_seconds": 1500,
        }
    )


    assert (
        result["import_complete"]
        is True
    )
