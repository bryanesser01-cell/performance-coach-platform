from unittest.mock import patch

from api.models.coach_context import CoachContext
from api.services.pipeline_steps.performance_intelligence_step import (
    PerformanceIntelligenceStep,
)


def test_builds_performance_intelligence():

    context = CoachContext(
        athlete_id=1,
    )

    context.athlete_state = {
        "training_sessions": [],
    }

    expected = {
        "performance_trend": {
            "trend": "improving",
        },
    }

    with patch(
        "api.services.pipeline_steps.performance_intelligence_step.generate_performance_insight"
    ) as mock_service:

        mock_service.return_value = expected

        PerformanceIntelligenceStep()(context)

        assert context.performance_intelligence == expected


def test_calls_performance_service():

    context = CoachContext(
        athlete_id=1,
    )

    context.athlete_state = {
        "training_sessions": [],
    }

    with patch(
        "api.services.pipeline_steps.performance_intelligence_step.generate_performance_insight"
    ) as mock_service:

        PerformanceIntelligenceStep()(context)

        mock_service.assert_called_once_with(
            [],
        )
