from api.services.unified_training_import_service import (
    build_training_import_result,
    import_training_session,
    select_adapter,
)


def test_select_garmin_adapter():

    result = select_adapter(
        "garmin"
    )

    assert (
        result
        == "garmin"
    )



def test_import_garmin_training():

    result = import_training_session(
        source="garmin",
        raw_data={
            "distance_meters": 5000,
            "duration_seconds": 1500,
            "average_hr": 145,
        },
    )


    assert (
        result["source"]
        == "garmin"
    )


    assert (
        result["training_session"]["distance_km"]
        == 5
    )



def test_unified_import_pipeline():

    result = build_training_import_result(
        source="apple_health",
        raw_data={
            "distance_km": 5,
            "duration_minutes": 25,
        },
    )


    assert (
        result["ready_for_coach"]
        is True
    )
