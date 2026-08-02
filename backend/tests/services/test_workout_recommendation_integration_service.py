from api.services.workout_recommendation_integration_service import (
    build_complete_workout_coach_context,
    get_workout_summary,
    needs_coach_adjustment,
)


def test_complete_workout_coach_context():

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

    context = build_complete_workout_coach_context(
        athlete_state=athlete_state,
        event="1500m",
        goal_time="4:45",
    )

    assert context["event"] == "1500m"

    assert "coach_message" in context

    assert context["recommendation"]["workout"]["session_type"] == "interval"


def test_workout_summary():

    context = {
        "recommendation": {
            "workout": {
                "workout": ("5 x 400m at race pace"),
                "athlete_explanation": {
                    "effort": "8-9/10",
                    "feeling": ("Fast and controlled."),
                    "purpose": ("Improve race pace."),
                },
            }
        }
    }

    summary = get_workout_summary(
        context,
    )

    assert summary["session"] == "5 x 400m at race pace"

    assert summary["effort"] == "8-9/10"


def test_low_readiness_needs_adjustment():

    athlete_state = {
        "readiness": {
            "score": 50,
        },
        "training": {
            "load_status": "normal",
        },
    }

    assert (
        needs_coach_adjustment(
            athlete_state,
        )
        is True
    )


def test_high_training_load_needs_adjustment():

    athlete_state = {
        "readiness": {
            "score": 80,
        },
        "training": {
            "load_status": "high",
        },
    }

    assert (
        needs_coach_adjustment(
            athlete_state,
        )
        is True
    )


def test_good_state_keeps_workout():

    athlete_state = {
        "readiness": {
            "score": 90,
        },
        "training": {
            "load_status": "optimal",
        },
    }

    assert (
        needs_coach_adjustment(
            athlete_state,
        )
        is False
    )
