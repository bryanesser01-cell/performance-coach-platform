from unittest.mock import patch

from api.models.coach_context import CoachContext
from api.services.pipeline_steps.periodisation_step import (
    PeriodisationStep,
)


def test_builds_periodisation():

    context = CoachContext(
        athlete_id=1,
    )

    context.race_intelligence = {
        "phase": "build",
    }

    expected = {
        "weekly_focus": "Endurance",
    }

    with patch(
        "api.services.pipeline_steps.periodisation_step.PeriodisationEngine"
    ) as mock_engine:

        mock_engine.return_value.build_plan.return_value = expected

        PeriodisationStep()(context)

        assert context.periodisation == expected


def test_calls_periodisation_engine():

    context = CoachContext(
        athlete_id=1,
    )

    context.race_intelligence = {
        "phase": "taper",
    }

    with patch(
        "api.services.pipeline_steps.periodisation_step.PeriodisationEngine"
    ) as mock_engine:

        PeriodisationStep()(context)

        mock_engine.return_value.build_plan.assert_called_once_with(
            context.race_intelligence,
        )
