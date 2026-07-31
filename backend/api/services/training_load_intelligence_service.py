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
            }

        acute = sum(
            session.get("training_load", 0)
            for session in sessions[-7:]
        )

        # At least 28 sessions are required before ACWR
        # becomes meaningful.
        if len(sessions) < 28:
            return {
                "acute_load": acute,
                "chronic_load": 0,
                "acwr": 0.0,
                "risk": "insufficient_data",
            }

        chronic = (
            sum(
                session.get("training_load", 0)
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

        elif acwr > 1.2:
            risk = "moderate"

        else:
            risk = "low"

        return {
            "acute_load": acute,
            "chronic_load": round(
                chronic,
                1,
            ),
            "acwr": acwr,
            "risk": risk,
        }
