from api.services.ai_coach_learning_loop_service import (
    run_learning_loop,
)


def capture_coach_learning_event(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Capture completed AI Coach interaction.
    """

    return {
        "athlete_id": athlete_id,
        "question": question,
        "decision": response.get(
            "decision",
            "",
        ),
        "confidence": response.get(
            "confidence",
            0,
        ),
        "outcome": response.get(
            "outcome",
        ),
    }


def process_coach_outcome(
    learning_event: dict,
) -> dict:
    """
    Send event through learning loop.
    """

    return run_learning_loop(
        athlete_id=learning_event[
            "athlete_id"
        ],
        question=learning_event[
            "question"
        ],
        decision=learning_event[
            "decision"
        ],
        confidence=learning_event[
            "confidence"
        ],
        outcome=learning_event.get(
            "outcome",
        ),
    )


def attach_learning_to_response(
    response: dict,
    learning_result: dict,
) -> dict:
    """
    Attach learning metadata.
    """

    return {
        **response,
        "learning_updated": True,
        "learning_signal": learning_result[
            "learning_signal"
        ],
        "learning_memory": learning_result[
            "memory"
        ],
    }


def integrate_coach_learning(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Complete learning integration flow.
    """

    learning_event = capture_coach_learning_event(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )

    learning_result = process_coach_outcome(
        learning_event,
    )

    return attach_learning_to_response(
        response=response,
        learning_result=learning_result,
    )
