from api.services.athlete_progress_timeline_service import (
    generate_progress_timeline,
)


def test_progress_timeline_detects_improvement():

    activities = [
        {
            "pace": 360,
        },
        {
            "pace": 340,
        },
    ]

    result = generate_progress_timeline(
        activities,
    )

    assert result["fitness_trend"] == "improving"


def test_progress_timeline_calculates_pace_change():

    activities = [
        {
            "pace": 360,
        },
        {
            "pace": 330,
        },
    ]

    result = generate_progress_timeline(
        activities,
    )

    assert result["pace_improvement_seconds_per_km"] == 30


def test_consistency_score():

    activities = [
        {"pace": 360},
        {"pace": 350},
        {"pace": 340},
    ]

    result = generate_progress_timeline(
        activities,
    )

    assert result["consistency_score"] == 30
