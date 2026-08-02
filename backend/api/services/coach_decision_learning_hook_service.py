from sqlalchemy.orm import Session

from api.services.coach_learning_capture_service import (
    capture_coach_decision_outcome,
)


def prepare_learning_hook(
    decision: str,
    athlete_id: int,
) -> dict:
    """
    Prepare learning tracking information
    after a coach decision.
    """

    return {
        "athlete_id": athlete_id,
        "decision": decision,
        "status": "awaiting_outcome",
    }


def process_coach_outcome(
    db: Session,
    athlete_id: int,
    decision: str,
    outcome: str,
) -> dict:
    """
    Process athlete outcome after
    a coaching decision.

    Flow:

    Decision
        ↓
    Outcome
        ↓
    Learning Event
        ↓
    Confidence Update
    """

    learning_event = capture_coach_decision_outcome(
        db=db,
        athlete_id=athlete_id,
        decision=decision,
        outcome=outcome,
    )

    return {
        "athlete_id": athlete_id,
        "decision": decision,
        "outcome": outcome,
        "learning_event": learning_event,
    }


def update_decision_confidence(
    decision_context: dict,
    learning_event: dict,
) -> dict:
    """
    Update decision confidence
    after learning feedback.
    """

    current_confidence = decision_context.get(
        "confidence",
        50,
    )

    confidence_change = learning_event.get(
        "confidence_change",
        0,
    )

    updated_confidence = current_confidence + confidence_change

    updated_confidence = max(
        0,
        min(
            updated_confidence,
            100,
        ),
    )

    return {
        **decision_context,
        "confidence": updated_confidence,
    }


def create_learning_hook_result(
    decision: str,
    athlete_id: int,
    confidence: int = 50,
) -> dict:
    """
    Create complete learning hook state.
    """

    return {
        "athlete_id": athlete_id,
        "decision": decision,
        "confidence": confidence,
        "learning_status": "active",
    }
