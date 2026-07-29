from api.services.coach_workout_planning_service import (
    build_coach_workout_plan,
    get_coach_workout_decision,
    should_skip_quality_session,
)


def test_build_coach_workout_plan():

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

    plan = build_coach_workout_plan(
        athlete_state=athlete_state,
        event="1500m",
        goal_time="4:45",
    )

    assert (
        plan["event"]
        == "1500m"
    )

    assert (
        plan["adjusted"]
        is False
    )

    assert (
        plan["workout"]
        ["session_type"]
        == "interval"
    )


def test_workout_adjusted_when_recovery_needed():

    athlete_state = {
        "readiness": {
            "score": 45,
        },
        "training": {
            "load_status": "high",
        },
    }

    plan = build_coach_workout_plan(
        athlete_state=athlete_state,
        event="1500m",
        goal_time="4:45",
    )

    assert (
        plan["adjusted"]
        is True
    )


def test_coach_decision_message():

    message = get_coach_workout_decision(
        {
            "adjusted": False,
        }
    )

    assert (
        "suitable"
        in message
    )


def test_skip_quality_session():

    athlete_state = {
        "readiness": {
            "score": 40,
        }
    }

    assert (
        should_skip_quality_session(
            athlete_state,
        )
        is True
    )


def test_keep_quality_session():

    athlete_state = {
        "readiness": {
            "score": 85,
        }
    }

    assert (
        should_skip_quality_session(
            athlete_state,
        )
        is False
    )
