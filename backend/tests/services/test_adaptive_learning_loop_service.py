from unittest.mock import MagicMock, patch

from api.services.adaptive_learning_loop_service import (
    process_adaptive_workout_outcome,
    record_adaptive_coaching_decision,
)


def test_record_adaptive_coaching_decision():

    db = MagicMock()

    decision = {
        "decision": "PROGRESS_TRAINING",
        "reason": "Performance improving.",
        "learning_confidence": 85,
    }

    with patch(
        "api.services.adaptive_learning_loop_service.record_coach_decision",
    ) as mock_record:

        mock_record.return_value = {
            "id": 1,
            "decision": "PROGRESS_TRAINING",
        }

        result = record_adaptive_coaching_decision(
            db=db,
            athlete_id=1,
            decision=decision,
        )

    assert result["decision"] == "PROGRESS_TRAINING"

    mock_record.assert_called_once_with(
        db=db,
        athlete_id=1,
        decision="PROGRESS_TRAINING",
        reason="Performance improving.",
        confidence=85,
    )


def test_process_adaptive_workout_outcome_positive():

    db = MagicMock()

    workout_result = {
        "completed": True,
        "rpe": 5,
        "fatigue": "low",
    }

    with patch(
        "api.services.adaptive_learning_loop_service.analyse_training_outcome",
    ) as mock_analysis, patch(
        "api.services.adaptive_learning_loop_service.process_coach_outcome",
    ) as mock_learning:

        mock_analysis.return_value = {
            "outcome": "positive",
        }

        mock_learning.return_value = {
            "confidence_update": 1,
            "outcome": "positive",
        }

        result = process_adaptive_workout_outcome(
            db=db,
            athlete_id=1,
            decision="PROGRESS_TRAINING",
            workout_result=workout_result,
        )

    assert result["athlete_id"] == 1

    assert result["decision"] == "PROGRESS_TRAINING"

    assert result["workout_analysis"]["outcome"] == "positive"

    assert result["learning_update"]["confidence_update"] == 1

    mock_learning.assert_called_once_with(
        db=db,
        athlete_id=1,
        decision="PROGRESS_TRAINING",
        outcome="positive",
    )


def test_process_adaptive_workout_outcome_negative():

    db = MagicMock()

    workout_result = {
        "completed": False,
        "rpe": 9,
        "fatigue": "high",
    }

    with patch(
        "api.services.adaptive_learning_loop_service.analyse_training_outcome",
    ) as mock_analysis, patch(
        "api.services.adaptive_learning_loop_service.process_coach_outcome",
    ) as mock_learning:

        mock_analysis.return_value = {
            "outcome": "negative",
        }

        mock_learning.return_value = {
            "confidence_update": -1,
            "outcome": "negative",
        }

        result = process_adaptive_workout_outcome(
            db=db,
            athlete_id=1,
            decision="PROGRESS_TRAINING",
            workout_result=workout_result,
        )

    assert result["workout_analysis"]["outcome"] == "negative"

    assert result["learning_update"]["confidence_update"] == -1

    mock_learning.assert_called_once_with(
        db=db,
        athlete_id=1,
        decision="PROGRESS_TRAINING",
        outcome="negative",
    )
