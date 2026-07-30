from api.services.daily_coach_recommendation_service import (
    build_daily_coach_message,
    generate_running_workout,
    generate_strength_workout,
)


def test_generate_running_workout():

    result = generate_running_workout(
        decision="TRAIN_HARD",
    )

    assert (
        result["running_workout"]["type"]
        == "intervals"
    )


def test_generate_strength_workout():

    result = generate_strength_workout()

    assert (
        result["session_type"]
        == "strength"
    )

    assert (
        result["exercises"][0]["name"]
        == "Squats"
    )

    assert (
        result["exercises"][0]["sets"]
        == 4
    )


def test_build_daily_coach_message():

    result = build_daily_coach_message(
        decision="TRAIN_MODERATE",
    )

    assert (
        result["decision"]
        == "TRAIN_MODERATE"
    )

    assert (
        len(result["sessions"])
        == 2
    )


def test_recovery_recommendation():

    result = build_daily_coach_message(
        decision="RECOVER",
        include_strength=False,
    )

    assert (
        result["sessions"][0]["session_type"]
        == "recovery"
    )
