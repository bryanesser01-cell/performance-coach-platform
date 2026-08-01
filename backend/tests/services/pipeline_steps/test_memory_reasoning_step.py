from unittest.mock import patch

from api.models.coach_context import CoachContext
from api.services.pipeline_steps.memory_reasoning_step import (
    MemoryReasoningStep,
)


def test_builds_memory_reasoning():

    context = CoachContext(
        athlete_id=1,
    )

    context.memory_context = {
        "sessions": [],
    }

    expected = {
        "fatigue_trend": "stable",
    }

    with patch(
        "api.services.pipeline_steps.memory_reasoning_step.MemoryReasoningService"
    ) as mock_service:

        mock_service.return_value.analyse.return_value = expected

        MemoryReasoningStep()(context)

        assert context.memory_reasoning == expected


def test_calls_memory_reasoning_service():

    context = CoachContext(
        athlete_id=1,
    )

    context.memory_context = {
        "sessions": [],
    }

    with patch(
        "api.services.pipeline_steps.memory_reasoning_step.MemoryReasoningService"
    ) as mock_service:

        MemoryReasoningStep()(context)

        mock_service.return_value.analyse.assert_called_once_with(
            context.memory_context,
        )
