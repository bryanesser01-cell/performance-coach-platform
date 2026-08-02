from api.services.workout_completion_analysis_service import (
    analyse_workout_completion,
    build_coach_feedback,
)


def test_completed_workout_with_high_fatigue():

    planned_workout = {
        "session": "5 x 400m",
        "target": "90 seconds",
    }

    athlete_feedback = {
        "completed": True,
        "rpe": 9,
        "target_hit": False,
        "difficulty": "very_hard",
        "comments": ("Last two reps were difficult"),
    }

    result = analyse_workout_completion(
        planned_workout,
        athlete_feedback,
    )

    assert result["coach_signal"] == ("REDUCE_TRAINING")

    assert result["fatigue_signal"] == ("high")

    assert result["execution_score"] < 100


def test_completed_workout_progression_signal():

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

    result = analyse_workout_completion(
        planned_workout,
        athlete_feedback,
    )

    assert result["coach_signal"] == ("PROGRESS_TRAINING")

    assert result["fatigue_signal"] == ("low")


def test_incomplete_workout_returns_recovery():

    result = analyse_workout_completion(
        {},
        {
            "completed": False,
        },
    )

    assert result["coach_signal"] == ("RECOVERY_SESSION")

    assert result["execution_score"] == 0


def test_build_coach_feedback():

    result = build_coach_feedback({"summary": ("Good workout execution.")})

    assert result == ("Good workout execution.")
