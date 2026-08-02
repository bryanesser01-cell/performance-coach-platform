from api.services.adaptive_coaching_engine_service import (
    run_adaptive_coaching_engine,
)


def build_adaptive_conversation_context(
    coach_context: dict,
    learning_memory: dict | None = None,
) -> dict:
    """
    Build adaptive coaching context
    for conversation responses.

    Combines:
    - Coach context
    - Learning history
    - Adaptive decision
    """

    if learning_memory is None:
        learning_memory = {}

    adaptive_result = run_adaptive_coaching_engine(
        coach_context=coach_context,
        learning_memory=learning_memory,
    )

    return {
        "adaptive_decision": adaptive_result,
        "learning_memory": learning_memory,
    }


def generate_adaptive_coach_message(
    adaptive_context: dict,
) -> str:
    """
    Convert adaptive decision into
    athlete-friendly message.
    """

    decision = adaptive_context.get(
        "adaptive_decision",
        {},
    )

    message = decision.get(
        "message",
        "",
    )

    if message:
        return message

    return (
        "Your training recommendation "
        "has been adjusted based on "
        "your current condition."
    )


def integrate_learning_into_response(
    response: dict,
    learning_memory: dict,
) -> dict:
    """
    Attach learning information to
    AI Coach response.
    """

    return {
        **response,
        "learning_memory": learning_memory,
        "learning_confidence": (
            learning_memory.get(
                "confidence_adjustment",
                50,
            )
        ),
    }


def generate_adaptive_conversation_response(
    coach_context: dict,
    learning_memory: dict | None = None,
) -> dict:
    """
    Complete adaptive conversation pipeline.

    Flow:

    Coach Context
          ↓
    Adaptive Engine
          ↓
    Learning Adjustment
          ↓
    Coach Message
    """

    adaptive_context = build_adaptive_conversation_context(
        coach_context=coach_context,
        learning_memory=learning_memory,
    )

    message = generate_adaptive_coach_message(
        adaptive_context,
    )

    response = {
        "message": message,
        "adaptive_context": adaptive_context,
    }

    return integrate_learning_into_response(
        response=response,
        learning_memory=learning_memory or {},
    )
