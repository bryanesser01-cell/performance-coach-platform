from unittest.mock import MagicMock, patch

from api.models.coach_context import CoachContext
from api.services.pipeline_steps.athlete_state_step import (
    AthleteStateStep,
)


def test_loads_athlete_state():

    context = CoachContext(
        athlete_id=1,
    )

    expected = {
        "athlete": {
            "id": 1,
        },
    }

    with patch(
        "api.services.pipeline_steps.athlete_state_step.get_athlete_state",
    ) as mock_state:

        mock_state.return_value = expected

        AthleteStateStep(
            MagicMock(),
        )(context)

        assert context.athlete_state == expected


def test_calls_state_service():

    context = CoachContext(
        athlete_id=99,
    )

    db = MagicMock()

    with patch(
        "api.services.pipeline_steps.athlete_state_step.get_athlete_state",
    ) as mock_state:

        AthleteStateStep(
            db,
        )(context)

        mock_state.assert_called_once_with(
            db,
            99,
        )
