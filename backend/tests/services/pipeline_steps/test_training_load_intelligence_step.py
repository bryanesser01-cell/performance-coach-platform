from unittest.mock import patch

from api.models.coach_context import CoachContext
from api.services.pipeline_steps.training_load_intelligence_step import (
    TrainingLoadIntelligenceStep,
)


def test_builds_training_load_intelligence():

    context = CoachContext(
        athlete_id=1,
    )

    context.athlete_state = {
        "training_sessions": [],
    }

    expected = {
        "risk": "low",
    }

    with patch(
        "api.services.pipeline_steps.training_load_intelligence_step.TrainingLoadIntelligenceService"
    ) as mock_service:

        mock_service.return_value.analyse.return_value = expected

        TrainingLoadIntelligenceStep()(context)

        assert (
            context.training_load_intelligence
            == expected
        )


def test_calls_training_load_service():

    context = CoachContext(
        athlete_id=1,
    )

    context.athlete_state = {
        "training_sessions": [],
    }

    with patch(
        "api.services.pipeline_steps.training_load_intelligence_step.TrainingLoadIntelligenceService"
    ) as mock_service:

        TrainingLoadIntelligenceStep()(context)

        mock_service.return_value.analyse.assert_called_once_with(
            [],
        )
