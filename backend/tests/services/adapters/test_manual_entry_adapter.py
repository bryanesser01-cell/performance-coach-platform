from api.services.adapters.manual_entry_adapter import (
    create_manual_race_result,
    create_manual_training_entry,
)


def test_manual_training_entry():

    result = create_manual_training_entry(
        date="2026-07-30",
        distance_km=5,
        duration_minutes=25,
        athlete_feedback="good",
    )

    assert (
        result["source"]
        == "manual"
    )

    assert (
        result["pace"]
        == "5:00/km"
    )

    assert (
        result["session_type"]
        == "run"
    )


def test_manual_race_result():

    result = create_manual_race_result(
        date="2026-07-30",
        event="1500m",
        result_time="5:00",
        distance_km=1.5,
    )

    assert (
        result["source"]
        == "manual"
    )

    assert (
        result["session_type"]
        == "race"
    )

    assert (
        result["event"]
        == "1500m"
    )
