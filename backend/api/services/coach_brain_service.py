"""
Coach Brain Service

Central intelligence engine for the AI Coach.
"""

from api.models.coach_context import CoachContext
from api.services.decision_explanation_service import (
    DecisionExplanationService,
)


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

        Supports both:
        - CoachContext
        - Legacy parameters
        """

        if context is not None:
            athlete_state = context.athlete_state
            memory_reasoning = context.memory_reasoning
            decision = context.decision

        athlete_state = athlete_state or {}
        memory_reasoning = memory_reasoning or {}
        decision = decision or {}

        result = {
            "summary": self._build_summary(
                athlete_state,
                memory_reasoning,
                decision,
            ),
            "decision": decision.get(
                "decision",
            ),
            "recommendation": decision.get(
                "recommendation",
                "",
            ).rstrip("."),
            #
            # Workout Recommendation Engine output
            #
            "recommended_workout": (context.training_plan if context else None),
            "confidence": self._build_confidence(
                context,
                decision,
            ),
            "today_focus": self._build_today_focus(
                context,
            ),
            "reasoning": (
                DecisionExplanationService().build(
                    context,
                )
            ),
            "risks": self._build_risks(
                context,
            ),
            "coach_message": self._build_coach_message(
                decision,
            ),
        }

        if context is not None:
            context.coach_brain = result

        return result

    #
    # Private Builders
    #

    def _build_summary(
        self,
        athlete_state: dict,
        memory_reasoning: dict,
        decision: dict,
    ) -> str:
        """
        Build a concise summary for the coach.
        """

        readiness = athlete_state.get(
            "readiness",
            {},
        ).get(
            "score",
            0,
        )

        fatigue = memory_reasoning.get(
            "fatigue_trend",
            "unknown",
        )

        injury = memory_reasoning.get(
            "injury_risk",
            "unknown",
        )

        recommendation = decision.get(
            "recommendation",
            "",
        ).rstrip(".")

        return (
            f"Readiness {readiness}. "
            f"Fatigue trend {fatigue}. "
            f"Injury risk {injury}. "
            f"Recommendation: "
            f"{recommendation}."
        )

    def _build_confidence(
        self,
        context: CoachContext | None,
        decision: dict,
    ):
        """
        Build confidence score.
        """

        if context and context.confidence:
            return context.confidence.get(
                "confidence",
                "medium",
            )

        if context and context.decision_scoring:
            return context.decision_scoring.get(
                "confidence",
                "medium",
            )

        return decision.get(
            "learning_confidence",
            0,
        )

    def _build_today_focus(
        self,
        context: CoachContext | None,
    ) -> str:
        """
        Determine today's training focus.
        """

        if context and context.periodisation:
            return context.periodisation.get(
                "weekly_focus",
                "General Training",
            )

        return "General Training"

    def _build_risks(
        self,
        context: CoachContext | None,
    ) -> list[str]:
        """
        Build list of current coaching risks.
        """

        if context is None:
            return []

        risks = []

        if (
            context.training_load_intelligence.get(
                "risk",
            )
            == "high"
        ):
            risks.append(
                "High training load.",
            )

        if (
            context.recovery_intelligence.get(
                "status",
            )
            == "poor"
        ):
            risks.append(
                "Poor recovery.",
            )

        if (
            context.memory_reasoning.get(
                "injury_risk",
            )
            == "high"
        ):
            risks.append(
                "Elevated injury risk.",
            )

        if (
            context.race_intelligence.get(
                "phase",
            )
            == "taper"
        ):
            risks.append(
                "Approaching race taper.",
            )

        return risks

    def _build_coach_message(
        self,
        decision: dict,
    ) -> str:
        """
        Generate athlete-facing coach message.
        """

        recommendation = decision.get(
            "recommendation",
            "",
        ).strip()

        if recommendation:
            return recommendation

        return "Continue following your current training plan."
