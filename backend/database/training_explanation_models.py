from api.services.training_explanation_service import (
    explain_workout,
    get_effort_description,
    get_training_explanation,
)


def test_threshold_explanation():

    explanation = get_training_explanation(
        "threshold",
    )

    assert (
        explanation["effort"]
        == "7/10"
    )

    assert (
        "controlled"
        in explanation["explanation"]
    )


def test_interval_explanation():

    explanation = get_training_explanation(
        "interval",
    )

    assert (
        explanation["effort"]
        == "8-9/10"
    )


def test_workout_gets_explanation():

    workout = {
        "session_type": "interval",
        "workout": (
            "5 x 400m"
        ),
    }

    result = explain_workout(
        workout,
    )

    assert (
        "athlete_explanation"
        in result
    )


def test_effort_description():

    description = get_effort_description(
        "7/10",
    )

    assert (
        "Strong"
        in description
    )
