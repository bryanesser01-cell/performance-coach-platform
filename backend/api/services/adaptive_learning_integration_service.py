from api.services.coach_learning_capture_service import (
    calculate_learning_update,
)
from api.services.coach_learning_service import (
    analyse_coach_decision_outcome,
)


def process_coach_learning_update(
    decision: str,
    completed: bool,
    athlete_rpe: int | None = None,
    fatigue_after: str | None = None,
) -> dict:
    """
    Process coaching decision outcome
    and create learning update.
    """

    learning_update = analyse_coach_decision_outcome(
        decision=decision,
        completed=completed,
        athlete_rpe=athlete_rpe,
        fatigue_after=fatigue_after,
    )

    confidence_change = calculate_learning_update(learning_update["signal"])

    return {
        "decision": decision,
        "learning_update": learning_update,
        "confidence_change": confidence_change,
        "learning_processed": True,
    }
