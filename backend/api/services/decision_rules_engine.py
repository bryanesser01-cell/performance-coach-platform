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
        # Athlete State
        #
        readiness = (
            context.athlete_state
            .get("readiness", {})
            .get("score", 0)
        )

        #
        # Memory
        #
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

        #
        # Goal Intelligence
        #
        goal_on_track = (
            context.goal_intelligence.get(
                "on_track",
                True,
            )
        )

        #
        # Performance Intelligence
        #
        performance = (
            context.performance_intelligence.get("trend")
            or context.performance_intelligence.get(
                "performance_trend",
                {},
            ).get(
                "trend",
                "stable",
            )
        )

        performance_recommendation = (
            context.performance_intelligence.get(
                "recommendation",
                "progress",
            )
        )

        #
        # Recovery Intelligence
        #
        recovery_status = (
            context.recovery_intelligence.get(
                "status",
                "good",
            )
        )

        #
        # Training Load Intelligence
        #
        training_risk = (
            context.training_load_intelligence.get(
                "risk",
                "low",
            )
        )

        #
        # Race Intelligence
        #
        race_phase = (
            context.race_intelligence.get(
                "phase",
                "base",
            )
        )

        #
        # Performance Prediction
        #
        prediction_confidence = (
            context.performance_prediction.get(
                "confidence",
                "medium",
            )
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
        if (
            fatigue == "increasing"
            and readiness < 60
        ):
            return {
                "decision": "REDUCE_VOLUME",
                "confidence": 95,
                "reason": "Accumulating fatigue.",
            }

        #
        # Rule 6
        #
        if (
            race_phase == "taper"
            and readiness >= 70
        ):
            return {
                "decision": "RACE_TAPER",
                "confidence": 95,
                "reason": "Taper period before race.",
            }

        #
        # Rule 6A
        #
        if (
            prediction_confidence == "high"
            and readiness >= 75
        ):
            return {
                "decision": "PROGRESS_TRAINING",
                "confidence": 90,
                "reason": (
                    "High confidence performance prediction."
                ),
            }

        #
        # Rule 6B
        #
        if (
            race_phase == "Peak"
            and training_risk == "moderate"
        ):
            return {
                "decision": "MAINTAIN_PLAN",
                "confidence": 90,
                "reason": (
                    "Maintain workload during peak phase."
                ),
            }

               #
        # Rule 7
        #
        if (
            readiness >= 80
            and performance == "improving"
            and injury == "low"
            and goal_on_track
            and performance_recommendation
            == "progress"
        ):
            return {
                "decision": "PROGRESS_TRAINING",
                "confidence": 95,
                "reason": (
                    "High readiness with improving "
                    "performance and goals on track."
                ),
            }
        return {
            "decision": "MAINTAIN_PLAN",
            "confidence": 80,
            "reason": "No rule triggered.",
        }
