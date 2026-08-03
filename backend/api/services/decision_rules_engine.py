"""
Decision Rules Engine

Responsible for applying deterministic coaching rules before
the Coach Brain generates the final response.
"""

from api.models.coach_context import CoachContext


class DecisionRulesEngine:
    """
    Applies deterministic coaching rules to determine the
    recommended coaching action.
    """

    def evaluate(
        self,
        context: CoachContext,
    ) -> dict:
        """
        Evaluate the current athlete context.
        """

        #
        # Athlete Digital Twin
        #
        twin = context.athlete_digital_twin

        #
        # Athlete State
        #
        readiness = twin.readiness_score()

        #
        # Memory
        #
        fatigue = twin.fatigue_trend()

        injury = twin.injury_risk()

        #
        # Goal Intelligence
        #
        goal_on_track = twin.is_goal_on_track()

        #
        # Performance Intelligence
        #
        performance = context.performance_intelligence.get(
            "trend",
        ) or context.performance_intelligence.get(
            "performance_trend",
            {},
        ).get(
            "trend",
            "stable",
        )

        performance_recommendation = context.performance_intelligence.get(
            "recommendation",
            "progress",
        )

        #
        # Recovery Intelligence
        #
        recovery_status = twin.recovery_status()

        #
        # Training Load Intelligence
        #
        training_risk = twin.training_risk()

        fatigue_score = context.training_load_intelligence.get(
            "fatigue_score",
            0,
        )

        acwr = context.training_load_intelligence.get(
            "acwr",
            1.0,
        )

        #
        # Race Intelligence
        #
        race_phase = twin.race_phase()

        #
        # Performance Prediction
        #
        prediction_confidence = context.performance_prediction.get(
            "confidence",
            "medium",
        )

        #
        # Rule 1
        #
        if readiness < 40:
            return {
                "decision": "RECOVERY_DAY",
                "confidence": 100,
                "reason": "Low readiness.",
            }

        #
        # Rule 2
        #
        if injury == "high":
            return {
                "decision": "RECOVERY_DAY",
                "confidence": 100,
                "reason": "High injury risk.",
            }

        #
        # Rule 3
        #
        if recovery_status == "poor":
            return {
                "decision": "RECOVERY_DAY",
                "confidence": 95,
                "reason": "Poor recovery status.",
            }

        #
        # Rule 3A
        #
        if fatigue_score >= 90:
            return {
                "decision": "RECOVERY_DAY",
                "confidence": 98,
                "reason": "Fatigue score is critically high.",
            }

        #
        # Rule 3B
        #
        if acwr >= 1.5:
            return {
                "decision": "REDUCE_VOLUME",
                "confidence": 97,
                "reason": (
                    "Acute training load is significantly higher " "than chronic load."
                ),
            }

        #
        # Rule 4
        #
        if training_risk == "high":
            return {
                "decision": "REDUCE_VOLUME",
                "confidence": 95,
                "reason": "High training load risk.",
            }

        #
        # Rule 5
        #
        if fatigue == "increasing" and readiness < 60:
            return {
                "decision": "REDUCE_VOLUME",
                "confidence": 95,
                "reason": "Accumulating fatigue.",
            }

        #
        # Rule 6
        #
        if race_phase == "taper" and readiness >= 70:
            return {
                "decision": "RACE_TAPER",
                "confidence": 95,
                "reason": "Taper period before race.",
            }

        #
        # Rule 6A
        #
        if prediction_confidence == "high" and readiness >= 75:
            return {
                "decision": "PROGRESS_TRAINING",
                "confidence": 90,
                "reason": "High confidence performance prediction.",
            }

        #
        # Rule 6B
        #
        if race_phase == "peak" and training_risk == "moderate":
            return {
                "decision": "MAINTAIN_PLAN",
                "confidence": 90,
                "reason": "Maintain workload during peak phase.",
            }

        #
        # Rule 7
        #
        if (
            readiness >= 80
            and performance == "improving"
            and injury == "low"
            and goal_on_track
            and performance_recommendation == "progress"
        ):
            return {
                "decision": "PROGRESS_TRAINING",
                "confidence": 95,
                "reason": (
                    "High readiness with improving " "performance and goals on track."
                ),
            }

        #
        # Default
        #
        return {
            "decision": "MAINTAIN_PLAN",
            "confidence": 80,
            "reason": "No rule triggered.",
        }
