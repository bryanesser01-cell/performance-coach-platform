from datetime import datetime, timezone


def record_coach_interaction(
    athlete_id: int,
    question: str,
    decision: str,
    confidence: int,
    outcome: str | None = None,
) -> dict:
    """
    Record AI Coach interaction.

    Stores the coaching event that can later
    be used for learning improvements.
    """

    return {
        "athlete_id": athlete_id,
        "question": question,
        "decision": decision,
        "confidence": confidence,
        "outcome": outcome,
        "recorded_at": datetime.now(
            timezone.utc
        ).isoformat(),
    }


def generate_learning_signal(
    decision: str,
    outcome: str | None,
    confidence: int,
) -> dict:
    """
    Generate a learning signal from the
    coaching outcome.

    Positive outcomes increase confidence.
    Negative outcomes reduce confidence.
    """

    if outcome == "positive":
        signal = "REINFORCE"

    elif outcome == "negative":
        signal = "ADJUST"

    else:
        signal = "WAIT_FOR_DATA"

    return {
        "decision": decision,
        "outcome": outcome,
        "confidence": confidence,
        "signal": signal,
    }


def update_learning_memory(
    athlete_id: int,
    learning_signal: dict,
) -> dict:
    """
    Update athlete learning memory.

    Future versions can persist this into
    the learning database.
    """

    return {
        "athlete_id": athlete_id,
        "learning_updated": True,
        "signal": learning_signal,
    }


def run_learning_loop(
    athlete_id: int,
    question: str,
    decision: str,
    confidence: int,
    outcome: str | None = None,
) -> dict:
    """
    Complete AI Coach learning loop.

    Flow:

    Coach Decision
          ↓
    Record Interaction
          ↓
    Generate Learning Signal
          ↓
    Update Memory
    """

    interaction = record_coach_interaction(
        athlete_id=athlete_id,
        question=question,
        decision=decision,
        confidence=confidence,
        outcome=outcome,
    )

    signal = generate_learning_signal(
        decision=decision,
        outcome=outcome,
        confidence=confidence,
    )

    memory = update_learning_memory(
        athlete_id=athlete_id,
        learning_signal=signal,
    )

    return {
        "interaction": interaction,
        "learning_signal": signal,
        "memory": memory,
    }
