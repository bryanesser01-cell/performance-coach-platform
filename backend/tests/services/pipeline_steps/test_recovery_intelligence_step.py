from unittest.mock import patch

from api.models.coach_context import CoachContext
from api.services.pipeline_steps.recovery_intelligence_step import (
    RecoveryIntelligenceStep,
)


def test_builds_recovery_intelligence():

    context = CoachContext(
        athlete_id=1,
    )

    context.athlete_state = {
        "readiness": {
            "score": 82,
        }
    }

    expected = {
        "status": "good",
    }

    with patch(
        "api.services.pipeline_steps.recovery_intelligence_step.generate_recovery_recommendation"
    ) as mock_service:

        mock_service.return_value = expected

        RecoveryIntelligenceStep()(context)

        assert context.recovery_intelligence == expected


def test_calls_recovery_service():

    context = CoachContext(
        athlete_id=1,
    )

    context.athlete_state = {
        "readiness": {
            "score": 70,
        }
    }

    with patch(
        "api.services.pipeline_steps.recovery_intelligence_step.generate_recovery_recommendation"
    ) as mock_service:

        RecoveryIntelligenceStep()(context)

        mock_service.assert_called_once_with(
            70,
        )
