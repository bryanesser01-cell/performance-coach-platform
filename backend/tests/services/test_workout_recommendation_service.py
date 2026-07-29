from api.services.workout_recommendation_service import (
    build_workout_recommendation,
    generate_workout_coach_message,
    should_adjust_workout,
)


def test_complete_workout_recommendation():

    athlete_state = {
        "readiness": {
            "score": 85,
        },
        "performance": {
            "trend": "improving",
        },
        "training": {
            "load_status": "optimal",
        },
    }

    result = build_workout_recommendation(
        athlete_state=athlete_state,
        event="1500m",
        goal_time="4:45",
    )

    assert (
        result["event"]
        == "1500m"
    )

    assert (
        result["workout"]["session_type"]
        == "interval"
    )

    assert (
        "athlete_explanation"
        in result["workout"]
    )


def test_workout_coach_message():

    recommendation = {
        "workout": {
            "workout": (
                "5 x 400m at race pace"
            ),
            "athlete_explanation": {
                "effort": "8-9/10",
                "feeling": (
                    "Fast and controlled."
                ),
                "purpose": (
                    "Improve speed."
                ),
            },
        }
    }

    message = generate_workout_coach_message(
        recommendation,
    )

    assert (
        "5 x 400m"
        in message
    )

    assert (
        "8-9/10"
        in message
    )


def test_low_readiness_adjusts_workout():

    athlete_state = {
        "readiness": {
            "score": 45,
        }
    }

    assert (
        should_adjust_workout(
            athlete_state,
        )
        is True
    )


def test_good_readiness_keeps_workout():

    athlete_state = {
        "readiness": {
            "score": 90,
        }
    }

    assert (
        should_adjust_workout(
            athlete_state,
        )
        is False
    )
