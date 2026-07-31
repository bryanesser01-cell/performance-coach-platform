from unittest.mock import MagicMock, patch

from api.services.adaptive_coaching_loop_service import (
    run_adaptive_coaching_cycle,
)
from api.services.adaptive_learning_loop_service import (
    process_adaptive_workout_outcome,
)


def test_full_adaptive_learning_cycle_positive():

    db = MagicMock()

    athlete_state = {
        "athlete": {
            "id": 1,
            "name": "Bryan",
        },
        "readiness": {
            "score": 85,
            "status": "ready",
        },
        "training": {
            "load_status": "stable",
        },
        "performance": {
            "trend": "improving",
        },
    }

    decision = {
        "decision": "PROGRESS_TRAINING",
        "recommendation": (
            "Progress training carefully."
        ),
        "reason": (
            "Performance and readiness "
            "are improving."
        ),
        "learning_confidence": 85,
    }

    with patch(
        "api.services.adaptive_coaching_loop_service.get_athlete_state",
    ) as mock_state, patch(
        "api.services.adaptive_coaching_loop_service.generate_adaptive_coach_decision",
    ) as mock_decision, patch(
        "api.services.adaptive_coaching_loop_service.record_adaptive_coaching_decision",
    ) as mock_record:

        mock_state.return_value = athlete_state

        mock_decision.return_value = decision

        mock_record.return_value = {
            "id": 1,
            "decision": "PROGRESS_TRAINING",
        }

        result = run_adaptive_coaching_cycle(
            db=db,
            athlete_id=1,
            planned_workout={
                "type": "intervals",
            },
            athlete_feedback={
                "completed": True,
            },
        )

    assert result["adaptive"] is True

    assert (
        result["decision"]["decision"]
        == "PROGRESS_TRAINING"
    )

    assert (
        result["athlete_state"]["readiness"]["score"]
        == 85
    )

    assert (
        result["decision_record"]["decision"]
        == "PROGRESS_TRAINING"
    )


def test_full_adaptive_learning_cycle_negative():

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

    assert (
        result["workout_analysis"]["outcome"]
        == "negative"
    )

    assert (
        result["learning_update"]["outcome"]
        == "negative"
    )

    assert (
        result["learning_recorded"]
        is True
    )
