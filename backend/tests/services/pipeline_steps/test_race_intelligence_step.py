from unittest.mock import patch

from api.models.coach_context import CoachContext
from api.services.pipeline_steps.race_intelligence_step import (
    RaceIntelligenceStep,
)


def test_builds_race_intelligence():

    context = CoachContext(
        athlete_id=1,
    )

    context.athlete_state = {
        "next_race": {
            "distance": "5K",
        },
    }

    expected = {
        "phase": "build",
    }

    with patch(
        "api.services.pipeline_steps.race_intelligence_step.RaceIntelligenceService"
    ) as mock_service:

        mock_service.return_value.analyse.return_value = expected

        RaceIntelligenceStep()(context)

        assert context.race_intelligence == expected


def test_calls_race_service():

    context = CoachContext(
        athlete_id=1,
    )

    context.athlete_state = {
        "next_race": {
            "distance": "5K",
        },
    }

    with patch(
        "api.services.pipeline_steps.race_intelligence_step.RaceIntelligenceService"
    ) as mock_service:

        RaceIntelligenceStep()(context)

        mock_service.return_value.analyse.assert_called_once_with(
            context.athlete_state["next_race"],
        )
