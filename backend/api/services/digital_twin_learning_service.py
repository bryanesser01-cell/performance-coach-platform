"""
Digital Twin Learning Service

Converts training outcomes into
Athlete Digital Twin updates.
"""


class DigitalTwinLearningService:
    """
    Updates athlete intelligence based
    on completed workout feedback.
    """

    def process_training_outcome(
        self,
        outcome: dict,
    ) -> dict:
        """
        Convert workout outcome into
        digital twin learning signals.
        """

        result = {
            "performance_update": {},
            "recovery_update": {},
            "training_update": {},
        }

        status = outcome.get(
            "outcome",
            "neutral",
        )

        if status == "positive":

            result["performance_update"] = {
                "trend": "improving",
            }

            result["training_update"] = {
                "training_tolerance": "increasing",
            }

            result["recovery_update"] = {
                "response": "good",
            }

        elif status == "negative":

            result["performance_update"] = {
                "trend": "declining",
            }

            result["training_update"] = {
                "training_tolerance": "decreasing",
            }

            result["recovery_update"] = {
                "response": "poor",
            }

        else:

            result["performance_update"] = {
                "trend": "stable",
            }

        return result
