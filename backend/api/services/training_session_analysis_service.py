from sqlalchemy.orm import Session

from api.services.coach_learning_memory_service import (
    record_learning_event,
)
from database.training_models import TrainingSession


def analyse_training_outcome(
    session: TrainingSession,
) -> dict:
    """
    Analyse completed training session outcome.

    Uses:
    - Session status
    - Athlete notes
    - Training response

    Future:
    - Garmin data
    - Heart rate
    - Load
    - Recovery
    """

    notes = session.notes.lower() if session.notes else ""

    if any(
        word in notes
        for word in [
            "strong",
            "easy",
            "good",
            "great",
            "comfortable",
        ]
    ):
        outcome = "positive"

    elif any(
        word in notes
        for word in [
            "hard",
            "struggled",
            "tired",
            "pain",
            "bad",
        ]
    ):
        outcome = "negative"

    else:
        outcome = "neutral"

    return {
        "session_id": session.id,
        "session_type": session.session_type,
        "focus": session.focus,
        "outcome": outcome,
    }


def generate_session_learning_event(
    db: Session,
    athlete_id: int,
    session: TrainingSession,
    decision: str,
) -> dict:
    """
    Convert training outcome into AI Coach learning.

    Example:

    Training completed well:
        confidence +10

    Training response poor:
        confidence -10
    """

    analysis = analyse_training_outcome(
        session,
    )

    if analysis["outcome"] == "positive":
        confidence_change = 10

    elif analysis["outcome"] == "negative":
        confidence_change = -10

    else:
        confidence_change = 0

    event = record_learning_event(
        db=db,
        athlete_id=athlete_id,
        decision=decision,
        outcome=analysis["outcome"],
        confidence_change=confidence_change,
    )

    return {
        "analysis": analysis,
        "learning_event": event,
    }


def recommend_next_adjustment(
    session: TrainingSession,
) -> dict:
    """
    Recommend next training adjustment.
    """

    analysis = analyse_training_outcome(
        session,
    )

    if analysis["outcome"] == "positive":
        recommendation = "Continue progression."

    elif analysis["outcome"] == "negative":
        recommendation = "Reduce load and prioritise recovery."

    else:
        recommendation = "Maintain current training approach."

    return {
        "session_id": session.id,
        "outcome": analysis["outcome"],
        "recommendation": recommendation,
    }
