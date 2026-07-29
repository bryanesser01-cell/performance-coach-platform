from api.services.training_progression_service import (
    determine_training_focus,
    recommend_next_workout,
)


def test_1500m_training_focus():

    result = determine_training_focus(
        "1500m",
    )

    assert result == (
        "speed endurance"
    )


def test_1500m_workout_recommendation():

    workout = recommend_next_workout(
        event="1500m",
        goal_time="4:45",
        readiness_score=85,
    )

    assert (
        workout["session_type"]
        == "interval"
    )

    assert (
        "400m"
        in workout["workout"]
    )


def test_recovery_when_low_readiness():

    workout = recommend_next_workout(
        event="1500m",
        readiness_score=40,
    )

    assert (
        workout["session_type"]
        == "recovery"
    )


def test_5k_training_recommendation():

    workout = recommend_next_workout(
        event="5K",
        goal_time="20:00",
        readiness_score=85,
    )

    assert (
        workout["session_type"]
        == "threshold"
    )
