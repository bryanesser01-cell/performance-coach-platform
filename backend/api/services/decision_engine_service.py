"""
Decision Engine Service

Determines today's coaching decision by combining
outputs from the various intelligence services.
"""


class DecisionEngineService:
    """
    AI Coach decision engine.

    Version 1 uses simple rule-based logic.

    Future versions will use weighted scoring
    and adaptive learning.
    """

    def make_decision(
        self,
        recovery_status: str,
        fatigue_score: float,
    ) -> dict:
        """
        Generate today's coaching decision.
        """

        #
        # Rule 1
        #
        if recovery_status == "ready" and fatigue_score < 80:
            return {
                "decision": "HARD_SESSION",
                "confidence": 90,
                "reason": [
                    "Recovery is high.",
                    "Fatigue is acceptable.",
                ],
                "recommendation": ("Proceed with today's hard session."),
            }

        #
        # Rule 2
        #
        if recovery_status == "moderate":

            return {
                "decision": "EASY_SESSION",
                "confidence": 85,
                "reason": [
                    "Recovery is moderate.",
                ],
                "recommendation": ("Complete an easy aerobic run."),
            }

        #
        # Rule 3
        #
        return {
            "decision": "REST_DAY",
            "confidence": 95,
            "reason": [
                "Recovery is poor.",
            ],
            "recommendation": ("Prioritise recovery today."),
        }
