from sqlalchemy.orm import Session

from api.services.coach_learning_memory_service import (
    record_learning_event,
)


def calculate_learning_update(
    outcome: str,
) -> int:
    """
    Calculate confidence adjustment
    from coaching outcome.
    """

    if outcome == "positive":

        return 10

    if outcome == "negative":

        return -10

    return 0


def capture_coach_decision_outcome(
    db: Session,
    athlete_id: int,
    decision: str,
    outcome: str,
) -> dict:
    """
    Capture the result of a coaching decision.

    Flow:
    Decision
        ↓
    Athlete Outcome
        ↓
    Confidence Adjustment
        ↓
    Learning Memory
    """

    confidence_change = (
        calculate_learning_update(
            outcome,
        )
    )

    event = record_learning_event(
        db=db,
        athlete_id=athlete_id,
        decision=decision,
        outcome=outcome,
        confidence_change=confidence_change,
    )

    return {
        "athlete_id": athlete_id,
        "decision": decision,
        "outcome": outcome,
        "confidence_change": confidence_change,
        "learning_event": event,
    }


def store_learning_feedback(
    db: Session,
    athlete_id: int,
    decision: str,
    completed: bool,
    performance_change: str,
) -> dict:
    """
    Store athlete feedback after coaching.

    Converts athlete response into
    learning outcome.
    """

    if completed and performance_change == "improved":

        outcome = "positive"

    elif performance_change == "worse":

        outcome = "negative"

    else:

        outcome = "neutral"

    return capture_coach_decision_outcome(
        db=db,
        athlete_id=athlete_id,
        decision=decision,
        outcome=outcome,
    )
