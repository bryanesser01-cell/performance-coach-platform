"""
Coach Brain Service

This service combines all coaching inputs into a single,
structured coaching decision.

Flow

Athlete State
      ↓
Memory Reasoning
      ↓
Decision Engine
      ↓
Coach Brain
"""


class CoachBrainService:
    """
    Central AI Coach reasoning engine.
    """

    def build_decision(
        self,
        athlete_state: dict,
        memory_reasoning: dict,
        decision: dict,
    ) -> dict:
        """
        Combine all coaching information into a
        single structured decision.
        """

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

        return {
            "summary": self._build_summary(
                readiness,
                memory_reasoning,
                decision,
            ),
            "recommendation": decision.get(
                "recommendation"
            ),
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

    def _build_summary(
        self,
        readiness: int,
        memory_reasoning: dict,
        decision: dict,
    ) -> str:

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

        return (
            f"Readiness {readiness}. "
            f"Fatigue trend {fatigue}. "
            f"Injury risk {injury}. "
            f"Recommendation: "
            f"{recommendation}."
        )
