from sqlalchemy.orm import Session

from database.repositories.coach_learning_repository import (
    calculate_confidence_adjustment,
    create_learning_event,
    get_learning_history,
)

_learning_history = []


def record_learning_event(
    athlete_id: int,
    decision: str,
    outcome: str,
    confidence_change: int,
    db: Session | None = None,
) -> dict:
    """
    Record AI Coach learning outcome.

    Supports:
    - Database persistence
    - Legacy adaptive coaching memory

    Stores:
    - Decision made
    - Athlete response/outcome
    - Confidence adjustment
    """

    if db is not None:

        event = create_learning_event(
            db=db,
            athlete_id=athlete_id,
            decision=decision,
            outcome=outcome,
            confidence_change=confidence_change,
        )

        return {
            "id": event.id,
            "athlete_id": event.athlete_id,
            "decision": event.decision,
            "outcome": event.outcome,
            "confidence_change": (event.confidence_change),
        }

    event = {
        "athlete_id": athlete_id,
        "decision": decision,
        "outcome": outcome,
        "confidence_change": confidence_change,
    }

    _learning_history.append(
        event,
    )

    return event


def build_learning_memory(
    db: Session,
    athlete_id: int,
) -> dict:
    """
    Build athlete learning memory context.

    Used by AI Coach decisions.
    """

    events = get_learning_history(
        db=db,
        athlete_id=athlete_id,
    )

    # Protect tests and empty database states
    if not isinstance(events, list):
        events = []

    confidence = calculate_confidence_adjustment(
        events,
    )

    return {
        "athlete_id": athlete_id,
        "learning_events": [
            {
                "decision": event.decision,
                "outcome": event.outcome,
                "confidence_change": (event.confidence_change),
            }
            for event in events
        ],
        "confidence_adjustment": confidence,
        "event_count": len(events),
    }


def get_learning_context(
    db: Session,
    athlete_id: int,
) -> dict:
    """
    Return learning context for AI Coach prompts.
    """

    return build_learning_memory(
        db=db,
        athlete_id=athlete_id,
    )


def calculate_learning_confidence(
    db: Session,
    athlete_id: int,
) -> int:
    """
    Calculate accumulated confidence
    from previous coaching outcomes.
    """

    events = get_learning_history(
        db=db,
        athlete_id=athlete_id,
    )

    return calculate_confidence_adjustment(
        events,
    )


def calculate_decision_confidence(
    decision: str,
    athlete_id: int | None = None,
    db: Session | None = None,
) -> int:
    """
    Calculate adaptive coaching confidence.

    Confidence starts at 50 and adjusts
    based on previous learning outcomes.
    """

    base_confidence = 50

    if db is not None and athlete_id is not None:

        events = get_learning_history(
            db=db,
            athlete_id=athlete_id,
        )

        matching_events = [event for event in events if event.decision == decision]

        adjustment = calculate_confidence_adjustment(
            matching_events,
        )

        return max(
            0,
            min(
                100,
                base_confidence + adjustment,
            ),
        )

    matching_events = [
        event
        for event in _learning_history
        if event["decision"] == decision
        and (athlete_id is None or event["athlete_id"] == athlete_id)
    ]

    adjustment = sum(event["confidence_change"] for event in matching_events)

    return max(
        0,
        min(
            100,
            base_confidence + adjustment,
        ),
    )
