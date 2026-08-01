from api.models.coach_context import CoachContext
from api.services.adaptive_coach_decision_service import (
    generate_adaptive_coach_decision,
)


class AdaptiveDecisionStep:
    """
    Generates the adaptive coaching decision.
    """

    def __call__(
        self,
        context: CoachContext,
    ) -> None:

        context.decision = (
            generate_adaptive_coach_decision(
                context=context,
            )
        )
