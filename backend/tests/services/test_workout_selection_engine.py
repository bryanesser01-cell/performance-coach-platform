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


def test_reduce_volume_returns_easy_run():

    engine = WorkoutSelectionEngine()

    result = engine.select_workout(
        twin=None,
        decision="REDUCE_VOLUME",
    )

    assert result["session_type"] == "Easy Run"


def test_taper_returns_taper_session():

    engine = WorkoutSelectionEngine()

    result = engine.select_workout(
        twin=None,
        decision="RACE_TAPER",
    )

    assert result["session_type"] == "Taper Session"
