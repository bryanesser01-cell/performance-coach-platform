"""
Digital Twin Update Service

Applies learning signals to the
Athlete Digital Twin.
"""


class DigitalTwinUpdateService:
    """
    Updates Athlete Digital Twin state
    from learning outcomes.
    """

    def apply_learning_update(
        self,
        twin,
        learning_update: dict,
    ):
        """
        Apply learning changes to twin.
        """

        performance = learning_update.get(
            "performance_update",
            {},
        )

        recovery = learning_update.get(
            "recovery_update",
            {},
        )

        training = learning_update.get(
            "training_update",
            {},
        )

        if performance:
            twin.performance_intelligence.update(
                performance,
            )

        if recovery:
            twin.recovery_intelligence.update(
                recovery,
            )

        if training:
            twin.training_load_intelligence.update(
                training,
            )

        return twin
