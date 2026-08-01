from api.models.coach_context import CoachContext
from api.services.decision_rules_engine import (
    DecisionRulesEngine,
)


class DecisionRulesStep:
    """
    Applies decision rules.
    """

    def __call__(
        self,
        context: CoachContext,
    ) -> None:

        context.decision = (
            DecisionRulesEngine()
            .evaluate(
                context,
            )
        )
