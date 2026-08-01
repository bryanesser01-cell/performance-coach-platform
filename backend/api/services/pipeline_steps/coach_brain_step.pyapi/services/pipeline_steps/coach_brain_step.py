from api.models.coach_context import CoachContext
from api.services.coach_brain_service import (
    CoachBrainService,
)


class CoachBrainStep:
    """
    Builds the final coach response.
    """

    def __call__(
        self,
        context: CoachContext,
    ) -> None:

        CoachBrainService().build_decision(
            context=context,
        )
