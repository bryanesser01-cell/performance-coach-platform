from api.models.coach_context import CoachContext


class TrainingPlanEngine:
    """
    Builds today's training plan.
    """

    def build(
        self,
        context: CoachContext,
    ) -> dict:

        decision = context.decision.get(
            "decision",
        )

        if decision == "RECOVERY_SESSION":
            return {
                "session_type": "Recovery",
                "duration": 40,
                "intensity": "Easy",
            }

        if decision == "PROGRESS_TRAINING":
            return {
                "session_type": "Workout",
                "duration": 60,
                "intensity": "Moderate",
            }

        return {
            "session_type": "Easy Run",
            "duration": 45,
            "intensity": "Easy",
        }
