from unittest.mock import MagicMock, patch

from api.services.ai_coach_orchestrator_service import (
    run_ai_coach_orchestrator,
)


def test_ai_coach_orchestrator_returns_athlete_state():

    athlete_state = {
        "athlete": {
            "id": 1,
            "name": "Bryan",
            "primary_event": "5K",
        },
        "readiness": {
            "score": 85,
            "status": "ready",
        },
    }

    decision = {
        "decision": "PROGRESS_TRAINING",
        "recommendation": (
            "Progress training carefully " "while maintaining recovery."
        ),
        "reason": ("Performance and readiness " "are improving."),
        "learning_confidence": 80,
    }

    with patch(
        "api.services.pipeline_steps.athlete_state_step.get_athlete_state",
    ) as mock_state, patch(
        "api.services.pipeline_steps.adaptive_decision_step.generate_adaptive_coach_decision",
    ) as mock_decision:

        mock_state.return_value = athlete_state

        mock_decision.return_value = decision

        result = run_ai_coach_orchestrator(
            db=MagicMock(),
            athlete_id=1,
        )

    assert result["athlete_id"] == 1

    assert result["athlete_state"] == athlete_state

    assert result["decision"]["decision"] == "PROGRESS_TRAINING"

    assert result["coach_message"] == (
        "Readiness 85. "
        "Fatigue trend stable. "
        "Injury risk low. "
        "Recommendation: "
        "Progress training carefully "
        "while maintaining recovery."
    )

    assert result["ai_coach"] is True


def test_ai_coach_orchestrator_calls_state_service():

    with patch(
        "api.services.pipeline_steps.athlete_state_step.get_athlete_state",
    ) as mock_state, patch(
        "api.services.pipeline_steps.adaptive_decision_step.generate_adaptive_coach_decision",
    ) as mock_decision:

        mock_state.return_value = {}

        mock_decision.return_value = {
            "decision": "RECOVERY_SESSION",
            "recommendation": "Recover",
        }

        run_ai_coach_orchestrator(
            db=MagicMock(),
            athlete_id=5,
        )

    mock_state.assert_called_once()

    mock_decision.assert_called_once()

    _, kwargs = mock_decision.call_args

    #
    # New architecture passes the CoachContext
    # instead of individual arguments.
    #
    assert "context" in kwargs

    context = kwargs["context"]

    assert context.athlete_id == 5


def test_ai_coach_orchestrator_returns_athlete_digital_twin():

    athlete_state = {
        "athlete": {
            "id": 1,
            "name": "Bryan",
        },
        "readiness": {
            "score": 85,
            "status": "ready",
        },
    }

    decision = {
        "decision": "PROGRESS_TRAINING",
        "recommendation": (
            "Proceed with today's hard session."
        ),
        "confidence": 90,
    }

    with patch(
        "api.services.pipeline_steps.athlete_state_step.get_athlete_state",
    ) as mock_state, patch(
        "api.services.pipeline_steps.adaptive_decision_step.generate_adaptive_coach_decision",
    ) as mock_decision:

        mock_state.return_value = athlete_state

        mock_decision.return_value = decision

        result = run_ai_coach_orchestrator(
            db=MagicMock(),
            athlete_id=1,
        )

    assert "athlete_digital_twin" in result

    assert result["athlete_digital_twin"] is not None

    assert (
        result["athlete_digital_twin"].athlete
        == athlete_state
    )
