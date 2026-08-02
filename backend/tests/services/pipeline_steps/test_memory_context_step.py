from unittest.mock import MagicMock, patch

from api.models.coach_context import CoachContext
from api.services.pipeline_steps.memory_context_step import (
    MemoryContextStep,
)


def test_loads_memory_context():

    context = CoachContext(
        athlete_id=1,
    )

    expected = {
        "sessions": [],
    }

    with patch(
        "api.services.pipeline_steps.memory_context_step.MemoryContextService"
    ) as mock_service:

        mock_service.return_value.build_context.return_value = expected

        MemoryContextStep(
            MagicMock(),
        )(context)

        assert context.memory_context == expected


def test_calls_memory_service():

    context = CoachContext(
        athlete_id=7,
    )

    db = MagicMock()

    with patch(
        "api.services.pipeline_steps.memory_context_step.MemoryContextService"
    ) as mock_service:

        MemoryContextStep(
            db,
        )(context)

        mock_service.return_value.build_context.assert_called_once_with(
            7,
        )
