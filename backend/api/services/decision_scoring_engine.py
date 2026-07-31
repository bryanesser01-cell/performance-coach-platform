"""
Decision Scoring Engine

Aggregates intelligence from multiple services into
weighted coaching recommendation scores.
"""

from api.models.coach_context import CoachContext


class DecisionScoringEngine:
    """
    Scores possible coaching decisions using weighted
    intelligence from the AI Coach pipeline.
    """

    def score(
        self,
        context: CoachContext,
    ) -> dict:
        """
        Calculate weighted scores for each possible
        coaching decision.
        """

        scores = {
            "RECOVERY_DAY": 0,
            "REDUCE_VOLUME": 0,
            "MAINTAIN_PLAN": 0,
            "PROGRESS_TRAINING": 0,
            "RACE_TAPER": 0,
        }

        reasons: list[str] = []

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
            reasons.append(
                "Very low readiness."
            )

        elif readiness < 60:
            scores["REDUCE_VOLUME"] += 50
            reasons.append(
                "Moderate readiness."
            )

        elif readiness >= 80:
            scores["PROGRESS_TRAINING"] += 30
            reasons.append(
                "High readiness."
            )

        #
        # Goal Intelligence
        #
        if context.goal_intelligence.get(
            "on_track",
            True,
        ):
            scores["PROGRESS_TRAINING"] += 20
            reasons.append(
                "Goal is on track."
            )
        else:
            scores["MAINTAIN_PLAN"] += 10
            reasons.append(
                "Goal needs attention."
            )

        #
        # Performance Intelligence
        #
        trend = (
            context.performance_intelligence.get(
                "trend",
                "stable",
            )
        )

        if trend == "improving":
            scores["PROGRESS_TRAINING"] += 20
            reasons.append(
                "Performance improving."
            )

        elif trend == "declining":
            scores["MAINTAIN_PLAN"] += 20
            reasons.append(
                "Performance declining."
            )

        #
        # Performance Prediction
        #
        if (
            context.performance_prediction.get(
                "confidence",
            )
            == "high"
        ):
            scores["PROGRESS_TRAINING"] += 10
            reasons.append(
                "High prediction confidence."
            )

        #
        # Recovery Intelligence
        #
        if (
            context.recovery_intelligence.get(
                "status",
            )
            == "poor"
        ):
            scores["RECOVERY_DAY"] += 40
            reasons.append(
                "Poor recovery."
            )

        #
        # Training Load Intelligence
        #
        risk = (
            context.training_load_intelligence.get(
                "risk",
                "low",
            )
        )

        if risk == "high":
            scores["REDUCE_VOLUME"] += 40
            reasons.append(
                "High training load."
            )

        elif risk == "moderate":
            scores["MAINTAIN_PLAN"] += 10
            reasons.append(
                "Moderate training load."
            )

        #
        # Race Intelligence
        #
        phase = (
            context.race_intelligence.get(
                "phase",
                "",
            )
        )

        if phase.lower() == "taper":
            scores["RACE_TAPER"] += 60
            reasons.append(
                "Taper phase."
            )

        #
        # Determine best decision
        #
        decision = max(
            scores,
            key=scores.get,
        )

        score = scores[
            decision
        ]

        #
        # Confidence
        #
        if score >= 80:
            confidence = "high"

        elif score >= 50:
            confidence = "medium"

        else:
            confidence = "low"

        #
        # Ranked decisions
        #
        ranking = sorted(
            scores.items(),
            key=lambda item: item[1],
            reverse=True,
        )

        return {
            "decision": decision,
            "score": score,
            "confidence": confidence,
            "scores": scores,
            "ranking": ranking,
            "reasons": reasons,
        }
