from api.models.coach_context import CoachContext


class ConfidenceStep:
    """
    Copies confidence into the shared context.
    """

    def __call__(
        self,
        context: CoachContext,
    ) -> None:

        context.confidence = {
            "confidence": (
                context.decision_scoring.get(
                    "confidence",
                    "medium",
                )
            )
        }
