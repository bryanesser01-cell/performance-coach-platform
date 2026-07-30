from api.services.training_adapter_service import (
    build_training_import_record,
    identify_training_source,
    normalise_training_session,
)


def test_garmin_conversion():

    result = normalise_training_session(
        source="garmin",
        raw_data={
            "distance_meters": 5000,
            "duration_seconds": 1500,
            "average_hr": 145,
        },
    )


    assert (
        result["distance_km"]
        == 5
    )

    assert (
        result["avg_heart_rate"]
        == 145
    )



def test_source_identification():

    result = identify_training_source(
        "garmin"
    )


    assert (
        result["supported"]
        is True
    )



def test_import_pipeline():

    result = build_training_import_record(
        source="manual",
        raw_data={
            "distance_km": 5,
            "duration_minutes": 25,
        },
    )


    assert (
        result["import_complete"]
        is True
    )
