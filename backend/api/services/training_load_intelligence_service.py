"""
Training Load Intelligence Service

Responsible for analysing training load and identifying
potential overtraining risk.

Current implementation:
- Requires at least 28 sessions before calculating ACWR.
- Uses the last 7 sessions as the acute workload.
- Uses the last 28 sessions to estimate the average weekly
  chronic workload.
"""


class TrainingLoadIntelligenceService:
    """
    Analyse acute and chronic training load.
    """

    def analyse(
        self,
        sessions: list[dict],
    ) -> dict:

        if not sessions:
            return {
                "acute_load": 0,
                "chronic_load": 0,
                "acwr": 0.0,
                "risk": "unknown",
                "load_status": "unknown",
                "recommendation": "collect_more_data",
                "confidence": 0.0,
            }

        acute = sum(
            session.get(
                "training_load",
                0,
            )
            for session in sessions[-7:]
        )

        #
        # Not enough history
        #
        if len(sessions) < 28:
            return {
                "acute_load": acute,
                "chronic_load": 0,
                "acwr": 0.0,
                "risk": "insufficient_data",
                "load_status": "building_history",
                "recommendation": "collect_more_data",
                "confidence": round(
                    len(sessions) / 28,
                    2,
                ),
                "sufficient_history": False,
            }

        chronic = (
            sum(
                session.get(
                    "training_load",
                    0,
                )
                for session in sessions[-28:]
            )
            / 4
        )

        acwr = round(
            acute / chronic,
            2,
        )

        if acwr > 1.5:
            risk = "high"
            recommendation = "reduce_training"

        elif acwr > 1.2:
            risk = "moderate"
            recommendation = "monitor_load"

        elif acwr >= 0.8:
            risk = "low"
            recommendation = "continue_plan"

        else:
            risk = "low"
            recommendation = "consider_progression"

        return {
            "acute_load": acute,
            "chronic_load": round(
                chronic,
                1,
            ),
            "acwr": acwr,
            "risk": risk,
            "load_status": risk,
            "recommendation": recommendation,
            "confidence": 1.0,
            "sufficient_history": True,
        }
