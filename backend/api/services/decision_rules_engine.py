"""
Decision Rules Engine

Responsible for applying deterministic coaching rules before
the Coach Brain generates the final response.
"""


class DecisionRulesEngine:
    """
    Applies coaching rules to determine the recommended action.
    """

    def evaluate(
        self,
        context,
    ) -> dict:
        """
        Evaluate athlete context and return a coaching decision.
        """

        readiness = (
            context.athlete_state
            .get("readiness", {})
            .get("score", 0)
        )

        fatigue = (
            context.memory_reasoning.get(
                "fatigue_trend",
                "stable",
            )
        )

        injury = (
            context.memory_reasoning.get(
                "injury_risk",
                "low",
            )
        )

        performance = (
            context.performance_intelligence.get(
                "performance_trend",
                {}
            ).get(
                "trend",
                "stable",
            )
        )

        # Rule 1
        if readiness < 40:
            return {
                "decision": "RECOVERY_DAY",
                "confidence": 100,
                "reason": "Low readiness.",
            }

        # Rule 2
        if injury == "high":
            return {
                "decision": "RECOVERY_DAY",
                "confidence": 100,
                "reason": "High injury risk.",
            }

        # Rule 3
        if (
            fatigue == "increasing"
            and readiness < 60
        ):
            return {
                "decision": "REDUCE_VOLUME",
                "confidence": 95,
                "reason": "Accumulating fatigue.",
            }

        # Rule 4
        if (
            readiness >= 80
            and performance == "improving"
            and injury == "low"
        ):
            return {
                "decision": "PROGRESS_TRAINING",
                "confidence": 95,
                "reason": "High readiness and improving fitness.",
            }

        return {
            "decision": "MAINTAIN_PLAN",
            "confidence": 80,
            "reason": "No rule triggered.",
        }
