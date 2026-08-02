from api.services.performance_intelligence_service import (
    analyse_performance_intelligence,
)


def test_builds_performance():

    sessions = [
        {
            "distance_km": 5,
            "duration_minutes": 25,
            "pace_seconds": 300,
        },
        {
            "distance_km": 5,
            "duration_minutes": 24,
            "pace_seconds": 288,
        },
    ]

    result = analyse_performance_intelligence(
        sessions,
    )

    assert isinstance(result, dict)
    assert "trend" in result
    assert "confidence" in result
    assert "average_pace" in result
