"""
Decision Scoring Engine

Aggregates intelligence from multiple services into
weighted coaching recommendation scores.
"""

from api.models.coach_context import CoachContext


class DecisionScoringEngine:
    """
    Scores possible coaching decisions.
    """

    def score(
        self,
        context: CoachContext,
    ) -> dict:

        scores = {
            "RECOVERY_DAY": 0,
            "REDUCE_VOLUME": 0,
            "MAINTAIN_PLAN": 0,
            "PROGRESS_TRAINING": 0,
            "RACE_TAPER": 0,
        }

        reasons = []

        #
        # Readiness
        #
        readiness = (
            context.athlete_state
            .get("readiness", {})
            .get("score", 0)
        )

        if readiness < 40:
            scores["RECOVERY_DAY"] += 100
            reasons.append("Very low readiness.")

        elif readiness < 60:
            scores["REDUCE_VOLUME"] += 50
            reasons.append("Moderate readiness.")

        elif readiness >= 80:
            scores["PROGRESS_TRAINING"] += 30
            reasons.append("High readiness.")

        #
        # Goal Intelligence
        #
        if context.goal_intelligence.get(
            "on_track",
            True,
        ):
            scores["PROGRESS_TRAINING"] += 20
        else:
            scores["MAINTAIN_PLAN"] += 10

        #
        # Recovery Intelligence
        #
        if (
            context.recovery_intelligence.get(
                "status"
            ) == "poor"
        ):
            scores["RECOVERY_DAY"] += 40
            reasons.append("Poor recovery.")

        #
        # Training Load
        #
        if (
            context.training_load_intelligence.get(
                "risk"
            ) == "high"
        ):
            scores["REDUCE_VOLUME"] += 40
            reasons.append("High training load.")

        #
        # Race Phase
        #
        if (
            context.race_intelligence.get(
                "phase"
            ) == "taper"
        ):
            scores["RACE_TAPER"] += 60
            reasons.append("Taper phase.")

        return {
            "scores": scores,
            "reasons": reasons,
        }
