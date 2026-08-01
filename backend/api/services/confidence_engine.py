"""
Confidence Engine

Calculates overall AI Coach confidence.
"""

from api.models.coach_context import CoachContext


class ConfidenceEngine:
    """
    Calculates confidence in today's coaching recommendation.
    """

    def calculate(
        self,
        context: CoachContext,
    ) -> dict:

        score = 50

        #
        # Readiness
        #
        readiness = (
            context.athlete_state
            .get("readiness", {})
            .get("score", 0)
        )

        if readiness >= 80:
            score += 10

        elif readiness < 50:
            score -= 10

        #
        # Performance prediction
        #
        if (
            context.performance_prediction.get(
                "confidence"
            )
            == "high"
        ):
            score += 15

        #
        # Recovery
        #
        if (
            context.recovery_intelligence.get(
                "status"
            )
            == "poor"
        ):
            score -= 10

        #
        # Training load
        #
        if (
            context.training_load_intelligence.get(
                "risk"
            )
            == "high"
        ):
            score -= 10

        #
        # Clamp
        #
        score = max(
            0,
            min(
                score,
                100,
            ),
        )

        if score >= 80:
            confidence = "high"

        elif score >= 60:
            confidence = "medium"

        else:
            confidence = "low"

        return {
            "score": score,
            "confidence": confidence,
        }
