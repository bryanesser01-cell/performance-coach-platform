"""
Coach Brain Service

Central intelligence engine for the AI Coach.
"""

from api.models.coach_context import CoachContext


class CoachBrainService:
    """
    Central AI Coach reasoning engine.

    Supports both the existing API and the newer
    CoachContext API during the migration.
    """

    def build_decision(
        self,
        context: CoachContext | None = None,
        athlete_state: dict | None = None,
        memory_reasoning: dict | None = None,
        decision: dict | None = None,
    ) -> dict:
        """
        Build the final coaching decision.

        During migration this supports:
        - CoachContext (new)
        - Separate dictionaries (legacy)
        """

        if context is not None:
            athlete_state = context.athlete_state
            memory_reasoning = context.memory_reasoning
            decision = context.decision

        athlete_state = athlete_state or {}
        memory_reasoning = memory_reasoning or {}
        decision = decision or {}

        readiness = (
            athlete_state.get("readiness", {})
            .get("score", 0)
        )

        training = athlete_state.get(
            "training",
            {},
        )

        performance = athlete_state.get(
            "performance",
            {},
        )

        fatigue = memory_reasoning.get(
            "fatigue_trend",
            "unknown",
        )

        injury = memory_reasoning.get(
            "injury_risk",
            "unknown",
        )

        recommendation = (
            decision.get(
                "recommendation",
                "",
            ).rstrip(".")
        )

        summary = (
            f"Readiness {readiness}. "
            f"Fatigue trend {fatigue}. "
            f"Injury risk {injury}. "
            f"Recommendation: "
            f"{recommendation}."
        )

        result = {
            "summary": summary,
            "recommendation": recommendation,
            "decision": decision.get(
                "decision"
            ),
            "confidence": decision.get(
                "learning_confidence",
                0,
            ),
            "reasoning": {
                "readiness": readiness,
                "training_load": training.get(
                    "load_status"
                ),
                "performance_trend": performance.get(
                    "trend"
                ),
                "memory": memory_reasoning,
            },
        }

        if context is not None:
            context.coach_brain = result

        return result
