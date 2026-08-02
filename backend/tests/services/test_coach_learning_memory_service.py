from datetime import datetime

_learning_history: list[dict] = []


def record_learning_event(
    athlete_id: int,
    decision: str,
    outcome: str,
    confidence_change: int,
) -> dict:
    """
    Store a coach learning event.

    Represents what happened after
    a coaching decision.
    """

    event = {
        "athlete_id": athlete_id,
        "decision": decision,
        "outcome": outcome,
        "confidence_change": confidence_change,
        "timestamp": datetime.utcnow().isoformat(),
    }

    _learning_history.append(
        event,
    )

    return event


def get_learning_history(
    athlete_id: int,
) -> list[dict]:
    """
    Retrieve learning history
    for an athlete.
    """

    return [event for event in _learning_history if event["athlete_id"] == athlete_id]


def calculate_decision_confidence(
    athlete_id: int,
    decision: str,
) -> int:
    """
    Calculate confidence score for
    a decision based on past outcomes.

    Starts at 50 and adjusts from
    previous learning events.
    """

    confidence = 50

    events = get_learning_history(
        athlete_id,
    )

    for event in events:

        if event["decision"] == decision:

            confidence += event["confidence_change"]

    return max(
        0,
        min(
            confidence,
            100,
        ),
    )
