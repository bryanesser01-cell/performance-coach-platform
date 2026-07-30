from sqlalchemy.orm import Session

from api.services.coach_learning_memory_service import (
    record_learning_event,
)


def record_coach_feedback(
    db: Session | None,
    athlete_id: int,
    decision: str,
    feedback: str,
) -> dict:
    """
    Record athlete feedback after a coach decision.

    Converts athlete feedback into
    a learning event.

    Positive feedback:
        confidence +10

    Negative feedback:
        confidence -10
    """

    feedback_lower = feedback.lower()

    if any(
        word in feedback_lower
        for word in [
            "worked",
            "good",
            "better",
            "great",
            "helped",
            "stronger",
        ]
    ):
        outcome = "positive"
        confidence_change = 10

    elif any(
        word in feedback_lower
        for word in [
            "bad",
            "worse",
            "too hard",
            "injured",
            "struggled",
        ]
    ):
        outcome = "negative"
        confidence_change = -10

    else:
        outcome = "neutral"
        confidence_change = 0

    event = record_learning_event(
        athlete_id=athlete_id,
        decision=decision,
        outcome=outcome,
        confidence_change=confidence_change,
        db=db,
    )

    return {
        "athlete_id": athlete_id,
        "decision": decision,
        "feedback": feedback,
        "outcome": outcome,
        "confidence_change": confidence_change,
        "learning_event": event,
    }


def analyse_feedback_sentiment(
    feedback: str,
) -> dict:
    """
    Analyse athlete feedback only.
    """

    feedback_lower = feedback.lower()

    if "good" in feedback_lower:
        sentiment = "positive"

    elif "bad" in feedback_lower:
        sentiment = "negative"

    else:
        sentiment = "neutral"

    return {
        "feedback": feedback,
        "sentiment": sentiment,
    }
