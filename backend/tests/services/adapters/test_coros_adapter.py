from api.services.adapters.coros_adapter import (
    build_coros_training_record,
    convert_coros_activity,
)


def test_convert_coros_activity():

    result = convert_coros_activity(
        {
            "activity_id": 456,
            "date": "2026-07-30",
            "distance_km": 10,
            "duration_minutes": 50,
            "average_hr": 150,
            "max_hr": 170,
            "cadence": 175,
        }
    )


    assert (
        result["source"]
        == "coros"
    )


    assert (
        result["distance_km"]
        == 10
    )


    assert (
        result["pace"]
        == "5:00/km"
    )



def test_coros_import_pipeline():

    result = build_coros_training_record(
        {
            "distance_km": 5,
            "duration_minutes": 25,
        }
    )


    assert (
        result["import_complete"]
        is True
    )
