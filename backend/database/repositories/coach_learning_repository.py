from sqlalchemy.orm import Session

from database.models import CoachLearningEvent


def create_learning_event(
    db: Session,
    athlete_id: int,
    decision: str,
    outcome: str,
    confidence_change: int,
) -> CoachLearningEvent:
    """
    Store a coach learning event.

    Records:
    - Decision made
    - Athlete outcome
    - Confidence adjustment
    """

    event = CoachLearningEvent(
        athlete_id=athlete_id,
        decision=decision,
        outcome=outcome,
        confidence_change=confidence_change,
    )

    db.add(
        event,
    )

    db.commit()

    db.refresh(
        event,
    )

    return event


def get_learning_history(
    db: Session,
    athlete_id: int,
    limit: int = 20,
) -> list[CoachLearningEvent]:
    """
    Retrieve previous coaching learning events
    for an athlete.
    """

    return (
        db.query(CoachLearningEvent)
        .filter(
            CoachLearningEvent.athlete_id
            == athlete_id,
        )
        .order_by(
            CoachLearningEvent.timestamp.desc(),
        )
        .limit(
            limit,
        )
        .all()
    )


def get_recent_decisions(
    db: Session,
    athlete_id: int,
    decision: str | None = None,
    limit: int = 10,
) -> list[CoachLearningEvent]:
    """
    Retrieve recent decisions of a type.
    """

    query = (
        db.query(CoachLearningEvent)
        .filter(
            CoachLearningEvent.athlete_id
            == athlete_id,
        )
    )

    if decision:

        query = query.filter(
            CoachLearningEvent.decision
            == decision,
        )

    return (
        query.order_by(
            CoachLearningEvent.timestamp.desc(),
        )
        .limit(
            limit,
        )
        .all()
    )


def calculate_confidence_adjustment(
    events: list[CoachLearningEvent],
) -> int:
    """
    Calculate confidence change from
    previous learning outcomes.
    """

    if not events:
        return 0

    return sum(
        event.confidence_change
        for event in events
    )
