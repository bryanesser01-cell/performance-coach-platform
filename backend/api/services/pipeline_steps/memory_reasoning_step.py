from api.models.coach_context import CoachContext
from api.services.memory_reasoning_service import (
    MemoryReasoningService,
)


class MemoryReasoningStep:
    """
    Analyses athlete memory context.
    """

    def __call__(
        self,
        context: CoachContext,
    ) -> None:

        context.memory_reasoning = (
            MemoryReasoningService()
            .analyse(
                context.memory_context,
            )
        )
