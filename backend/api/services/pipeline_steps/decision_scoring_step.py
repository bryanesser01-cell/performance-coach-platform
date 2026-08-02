from api.models.coach_context import CoachContext
from api.services.decision_scoring_engine import (
    DecisionScoringEngine,
)


class DecisionScoringStep:
    """
    Scores the coaching decision.
    """

    def __call__(
        self,
        context: CoachContext,
    ) -> None:

        context.decision_scoring = DecisionScoringEngine().score(
            context,
        )
