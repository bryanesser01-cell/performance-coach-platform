"""
Athlete Feedback Loop Service

Connects completed workouts,
learning signals, and Digital Twin updates.
"""

from api.services.training_session_analysis_service import (
    analyse_training_outcome,
)
from api.services.digital_twin_learning_service import (
    DigitalTwinLearningService,
)
from api.services.digital_twin_update_service import (
    DigitalTwinUpdateService,
)


class AthleteFeedbackLoopService:
    """
    Processes completed athlete sessions
    and updates learning state.
    """

    def process_completed_workout(
        self,
        twin,
        session,
    ) -> dict:
        """
        Process a completed workout.

        Flow:

        Session
          |
          ▼
        Analyse outcome
          |
          ▼
        Generate learning signal
          |
          ▼
        Update Digital Twin
        """

        analysis = analyse_training_outcome(
            session,
        )

        learning_update = (
            DigitalTwinLearningService()
            .process_training_outcome(
                outcome=analysis,
            )
        )

        updated_twin = (
            DigitalTwinUpdateService()
            .apply_learning_update(
                twin=twin,
                learning_update=learning_update,
            )
        )

        return {
            "analysis": analysis,
            "learning_update": learning_update,
            "digital_twin": updated_twin,
        }
