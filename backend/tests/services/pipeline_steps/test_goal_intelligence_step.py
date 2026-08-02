from unittest.mock import patch

from api.models.coach_context import CoachContext
from api.services.pipeline_steps.goal_intelligence_step import (
    GoalIntelligenceStep,
)


def test_builds_goal_intelligence():

    context = CoachContext(
        athlete_id=1,
    )

    context.athlete_state = {
        "goal": "5K PB",
    }

    expected = {
        "on_track": True,
    }

    with patch(
        "api.services.pipeline_steps.goal_intelligence_step.GoalIntelligenceService"
    ) as mock_service:

        mock_service.return_value.analyse.return_value = expected

        GoalIntelligenceStep()(context)

        assert context.goal_intelligence == expected


def test_calls_goal_service():

    context = CoachContext(
        athlete_id=1,
    )

    context.athlete_state = {}

    with patch(
        "api.services.pipeline_steps.goal_intelligence_step.GoalIntelligenceService"
    ) as mock_service:

        GoalIntelligenceStep()(context)

        mock_service.return_value.analyse.assert_called_once_with(
            context.athlete_state,
        )
