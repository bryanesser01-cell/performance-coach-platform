from api.services.training_data_service import (
    calculate_running_pace,
    calculate_session_load,
    create_training_session,
    summarise_training_week,
)


def test_calculate_running_pace():

    result = calculate_running_pace(
        distance_km=5,
        duration_minutes=25,
    )

    assert (
        result
        == "5:00/km"
    )



def test_calculate_session_load():

    result = calculate_session_load(
        duration_minutes=30,
        intensity=2,
    )

    assert (
        result
        == 60
    )



def test_create_training_session():

    result = create_training_session(
        session_date="2026-07-30",
        distance_km=5,
        duration_minutes=25,
        avg_heart_rate=145,
        athlete_feedback="good",
    )

    assert (
        result["pace"]
        == "5:00/km"
    )

    assert (
        result["session_type"]
        == "run"
    )



def test_training_week_summary():

    result = summarise_training_week(
        [
            {
                "distance_km": 5,
                "duration_minutes": 25,
                "training_load": 50,
            }
        ]
    )

    assert (
        result["total_distance_km"]
        == 5
    )
