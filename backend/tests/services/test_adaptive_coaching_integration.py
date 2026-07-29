from api.services.adaptive_coaching_loop_service import (
    run_adaptive_coaching_loop,
)


def test_adaptive_coaching_integration_reduces_training():

    planned_workout = {
        "session": "5 x 400m",
        "target": "90 seconds",
    }

    athlete_feedback = {
        "completed": True,
        "rpe": 9,
        "target_hit": False,
        "difficulty": "very_hard",
        "comments": (
            "Could not maintain pace "
            "on final repetitions."
        ),
    }

    result = run_adaptive_coaching_loop(
        planned_workout=planned_workout,
        athlete_feedback=athlete_feedback,
        readiness_score=55,
        training_load_status="high_fatigue",
        performance_trend="stable",
    )

    assert (
        result["coach_decision"]["decision"]
        == "REDUCE_TRAINING"
    )

    assert (
        result["workout_analysis"]["fatigue_signal"]
        == "high"
    )

    assert (
        result["recommendation"]
        is not None
    )


def test_adaptive_coaching_integration_progresses_training():

    planned_workout = {
        "session": "6 x 400m",
        "target": "90 seconds",
    }

    athlete_feedback = {
        "completed": True,
        "rpe": 6,
        "target_hit": True,
        "difficulty": "manageable",
        "comments": (
            "Workout felt controlled."
        ),
    }

    result = run_adaptive_coaching_loop(
        planned_workout=planned_workout,
        athlete_feedback=athlete_feedback,
        readiness_score=85,
        training_load_status="stable",
        performance_trend="improving",
    )

    assert (
        result["coach_decision"]["decision"]
        == "PROGRESS_TRAINING"
    )


def test_adaptive_coaching_integration_race_taper():

    result = run_adaptive_coaching_loop(
        planned_workout={
            "session": "Race preparation"
        },
        athlete_feedback={
            "completed": True,
            "rpe": 5,
            "target_hit": True,
        },
        readiness_score=90,
        training_load_status="stable",
        performance_trend="improving",
        days_to_race=7,
    )

    assert (
        result["coach_decision"]["decision"]
        == "RACE_TAPER"
    )
