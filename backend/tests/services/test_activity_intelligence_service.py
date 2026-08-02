from api.services.activity_intelligence_service import (
    analyse_activity,
    calculate_training_stress,
    detect_fitness_trend,
    generate_activity_learning_event,
)
from database.models import Activity


def create_activity():
    return Activity(
        id=1,
        athlete_id=1,
        source="garmin",
        category="run",
        name="Morning Run",
    )


def test_calculate_training_stress():

    result = calculate_training_stress(
        duration_seconds=3600,
        intensity="hard",
    )

    assert result == 180


def test_analyse_activity():

    activity = create_activity()

    result = analyse_activity(
        activity=activity,
        duration_seconds=1800,
        intensity="moderate",
    )

    assert result["activity_id"] == 1

    assert result["training_stress"] == 60


def test_detect_improving_fitness_trend():

    result = detect_fitness_trend(
        [
            {
                "training_stress": 50,
            },
            {
                "training_stress": 100,
            },
        ]
    )

    assert result["trend"] == "improving"


def test_generate_activity_learning_event():

    result = generate_activity_learning_event(
        {
            "activity_id": 1,
            "training_stress": 200,
        }
    )

    assert result["outcome"] == "high_load"
