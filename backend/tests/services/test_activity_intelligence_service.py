from api.services.activity_intelligence_service import (
    calculate_acute_load,
    calculate_training_stress,
    detect_fitness_trend,
)


def test_calculate_training_stress():
    activities = [
        {"training_stress": 100},
        {"training_stress": 150},
        {"training_stress": 75},
    ]

    assert calculate_training_stress(activities) == 325


def test_calculate_training_stress_empty():
    assert calculate_training_stress([]) == 0


def test_detect_fitness_trend_improving():
    result = detect_fitness_trend(
        [
            {"training_stress": 100},
            {"training_stress": 150},
        ]
    )

    assert result["trend"] == "improving"


def test_detect_fitness_trend_declining():
    result = detect_fitness_trend(
        [
            {"training_stress": 150},
            {"training_stress": 100},
        ]
    )

    assert result["trend"] == "declining"


def test_detect_fitness_trend_stable():
    result = detect_fitness_trend(
        [
            {"training_stress": 120},
            {"training_stress": 120},
        ]
    )

    assert result["trend"] == "stable"


def test_calculate_acute_load():
    activities = [
        {"training_stress": 120},
        {"training_stress": 80},
        {"training_stress": 100},
    ]

    assert (
        calculate_acute_load(
            activities,
        )
        == 300
    )
