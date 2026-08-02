from api.services.adaptive_coaching_loop_service import (
    run_adaptive_coaching_loop,
)


def test_adaptive_loop_reduces_training_after_hard_workout():

    planned_workout = {
        "session": "5 x 400m",
        "target": "90 seconds",
    }

    athlete_feedback = {
        "completed": True,
        "rpe": 9,
        "target_hit": False,
        "difficulty": "very_hard",
        "comments": ("Last reps were difficult"),
    }

    result = run_adaptive_coaching_loop(
        planned_workout=planned_workout,
        athlete_feedback=athlete_feedback,
        readiness_score=55,
        training_load_status="high_fatigue",
        performance_trend="stable",
    )

    assert result["workout_analysis"]["fatigue_signal"] == "high"

    assert result["coach_decision"]["decision"] == "REDUCE_TRAINING"


def test_adaptive_loop_progresses_training():

    planned_workout = {
        "session": "6 x 400m",
        "target": "90 seconds",
    }

    athlete_feedback = {
        "completed": True,
        "rpe": 6,
        "target_hit": True,
        "difficulty": "manageable",
        "comments": ("Felt controlled"),
    }

    result = run_adaptive_coaching_loop(
        planned_workout=planned_workout,
        athlete_feedback=athlete_feedback,
        readiness_score=85,
        training_load_status="stable",
        performance_trend="improving",
    )

    assert result["coach_decision"]["decision"] == "PROGRESS_TRAINING"


def test_adaptive_loop_race_taper():

    result = run_adaptive_coaching_loop(
        planned_workout={},
        athlete_feedback={
            "completed": True,
            "rpe": 5,
            "target_hit": True,
        },
        readiness_score=90,
        training_load_status="stable",
        performance_trend="improving",
        days_to_race=10,
    )

    assert result["coach_decision"]["decision"] == "RACE_TAPER"
