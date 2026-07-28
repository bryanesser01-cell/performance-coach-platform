from api.services.performance_trend_service import (
    generate_performance_trends,
)


def test_generate_performance_trends():
    activities = [
        {
            "distance_km": 5,
            "average_pace": 320,
            "training_load": 50,
        },
        {
            "distance_km": 10,
            "average_pace": 300,
            "training_load": 80,
        },
    ]

    result = generate_performance_trends(
        activities,
    )

    assert result["distance_trend"] == "increasing"
    assert result["pace_trend"] == "improving"
    assert result["training_load_trend"] == "increasing"
