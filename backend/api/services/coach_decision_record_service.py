from sqlalchemy.orm import Session

from database.models import CoachDecision


def record_coach_decision(
    db: Session,
    athlete_id: int,
    decision: str,
    reason: str,
    confidence: int,
) -> dict:
    """
    Store AI Coach decision.

    Creates permanent decision history.
    """

    coach_decision = CoachDecision(
        athlete_id=athlete_id,
        decision=decision,
        reason=reason,
        confidence=confidence,
    )

    db.add(
        coach_decision,
    )

    db.commit()

    db.refresh(
        coach_decision,
    )

    return {
        "id": coach_decision.id,
        "athlete_id": coach_decision.athlete_id,
        "decision": coach_decision.decision,
        "reason": coach_decision.reason,
        "confidence": coach_decision.confidence,
    }


def get_coach_decision_history(
    db: Session,
    athlete_id: int,
) -> list:
    """
    Retrieve previous AI Coach decisions.
    """

    decisions = (
        db.query(CoachDecision)
        .filter(
            CoachDecision.athlete_id
            == athlete_id,
        )
        .order_by(
            CoachDecision.created_at.desc(),
        )
        .all()
    )

    return [
        {
            "decision": item.decision,
            "reason": item.reason,
            "confidence": item.confidence,
        }
        for item in decisions
    ]


def calculate_average_decision_confidence(
    history: list[dict],
) -> int:
    """
    Calculate average AI decision confidence.
    """

    if not history:
        return 0

    total = sum(
        item["confidence"]
        for item in history
    )

    return int(
        total / len(history)
    )
