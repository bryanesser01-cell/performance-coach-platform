from api.services.workout_selection_engine import (
    WorkoutSelectionEngine,
)


def test_progress_training_without_twin_returns_threshold():

    engine = WorkoutSelectionEngine()

    result = engine.select_workout(
        twin=None,
        decision="PROGRESS_TRAINING",
    )

    assert result["session_type"] == "Threshold Run"


def test_recovery_returns_recovery_run():

    engine = WorkoutSelectionEngine()

    result = engine.select_workout(
        twin=None,
        decision="RECOVERY_DAY",
    )

    assert result["session_type"] == "Recovery Run"
