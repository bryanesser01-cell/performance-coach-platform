from api.services.athlete_performance_summary_service import (
    calculate_average_pace,
    calculate_training_load,
    calculate_weekly_distance,
    generate_performance_summary,
)


def test_calculate_weekly_distance():
    activities = [
        {
            "distance_km": 5,
        },
        {
            "distance_km": 10,
        },
    ]

    assert (
        calculate_weekly_distance(
            activities,
        )
        == 15
    )


def test_calculate_average_pace():
    activities = [
        {
            "distance_km": 5,
            "duration_seconds": 1500,
        },
    ]

    assert (
        calculate_average_pace(
            activities,
        )
        == 300
    )


def test_calculate_training_load():
    activities = [
        {
            "training_load": 50,
        },
        {
            "training_load": 70,
        },
    ]

    assert (
        calculate_training_load(
            activities,
        )
        == 120
    )


def test_generate_performance_summary():
    summary = generate_performance_summary(
        [
            {
                "distance_km": 5,
                "duration_seconds": 1500,
                "training_load": 50,
            }
        ],
    )

    assert summary["weekly_distance_km"] == 5
    assert summary["training_load"] == 50
