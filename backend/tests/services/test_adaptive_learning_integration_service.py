from api.services.adaptive_learning_integration_service import (
    process_coach_learning_update,
)


def test_positive_learning_update_after_successful_decision():

    result = process_coach_learning_update(
        decision="REDUCE_TRAINING",
        completed=True,
        athlete_rpe=4,
        fatigue_after="low",
    )

    assert result["learning_update"]["signal"] == "positive"

    assert result["learning_update"]["confidence_update"] == 1


def test_negative_learning_update_after_poor_outcome():

    result = process_coach_learning_update(
        decision="PROGRESS_TRAINING",
        completed=True,
        athlete_rpe=9,
        fatigue_after="high",
    )

    assert result["learning_update"]["signal"] == "negative"

    assert result["learning_update"]["confidence_update"] == -1


def test_learning_update_handles_incomplete_workout():

    result = process_coach_learning_update(
        decision="PROGRESS_TRAINING",
        completed=False,
    )

    assert result["learning_update"]["signal"] == "negative"


def test_learning_update_contains_original_decision():

    result = process_coach_learning_update(
        decision="REDUCE_TRAINING",
        completed=True,
        athlete_rpe=5,
        fatigue_after="low",
    )

    assert result["decision"] == "REDUCE_TRAINING"
