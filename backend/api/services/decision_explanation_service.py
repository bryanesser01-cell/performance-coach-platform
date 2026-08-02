"""
Decision Explanation Service

Builds explainable AI output for coaching decisions.
"""

from api.models.coach_context import CoachContext


class DecisionExplanationService:
    """
    Produces structured explanations for
    AI coaching decisions.
    """

    def build(
        self,
        context: CoachContext,
    ) -> dict:
        """
        Build explainable reasoning for the
        current coaching decision.
        """

        #
        # Readiness
        #
        readiness = context.athlete_state.get(
            "readiness",
            {},
        ).get(
            "score",
            0,
        )

        #
        # Performance
        #
        # Support both the new Performance Intelligence
        # service and the legacy Athlete State during
        # migration.
        #
        performance = context.performance_intelligence.get(
            "trend",
        ) or context.athlete_state.get(
            "performance",
            {},
        ).get(
            "trend",
            "stable",
        )

        #
        # Training Load
        #
        training_load = context.training_load_intelligence.get(
            "risk",
            "low",
        )

        #
        # Recovery
        #
        recovery = context.recovery_intelligence.get(
            "status",
            "good",
        )

        #
        # Race
        #
        race_phase = context.race_intelligence.get(
            "phase",
            "base",
        )

        #
        # Memory
        #
        fatigue = context.memory_reasoning.get(
            "fatigue_trend",
            "stable",
        )

        injury = context.memory_reasoning.get(
            "injury_risk",
            "low",
        )

        strengths: list[str] = []

        watch_items: list[str] = []

        #
        # Readiness
        #
        if readiness >= 80:
            strengths.append(
                "High readiness",
            )

        elif readiness < 60:
            watch_items.append(
                "Low readiness",
            )

        #
        # Performance
        #
        if performance == "improving":
            strengths.append(
                "Performance improving",
            )

        elif performance == "declining":
            watch_items.append(
                "Performance declining",
            )

        #
        # Fatigue
        #
        if fatigue == "increasing":
            watch_items.append(
                "Fatigue increasing",
            )

        #
        # Injury
        #
        if injury == "high":
            watch_items.append(
                "Elevated injury risk",
            )

        #
        # Training Load
        #
        if training_load == "high":
            watch_items.append(
                "High training load",
            )

        #
        # Recovery
        #
        if recovery == "poor":
            watch_items.append(
                "Recovery below optimal",
            )

        return {
            "strengths": strengths,
            "watch_items": watch_items,
            "evidence": {
                "readiness": readiness,
                "performance": performance,
                "training_load": training_load,
                "recovery": recovery,
                "race_phase": race_phase,
                "fatigue": fatigue,
                "injury": injury,
            },
        }
