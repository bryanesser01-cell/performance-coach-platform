from api.services.coach_decision_engine_service import (
    generate_coach_decision,
)


def build_adaptive_training_decision(
    coach_context: dict,
) -> dict:
    """
    Build adaptive coaching decision
    from unified coach context.

    Uses:
    - Recovery readiness
    - Training stress
    - Fitness trend
    - Learning confidence
    """

    summary = coach_context.get(
        "summary",
        {},
    )

    decision = generate_coach_decision(
        readiness_score=summary.get(
            "readiness_score",
            0,
        ),
        training_stress=summary.get(
            "training_stress",
            0,
        ),
        fitness_trend=summary.get(
            "fitness_trend",
            "unknown",
        ),
        learning_confidence=summary.get(
            "learning_confidence",
            50,
        ),
    )

    return decision


def apply_learning_adjustment(
    decision: dict,
    learning_memory: dict,
) -> dict:
    """
    Adjust coaching confidence using
    previous learning outcomes.
    """

    confidence = learning_memory.get(
        "confidence_adjustment",
        0,
    )

    original_confidence = decision.get(
        "learning_confidence",
        50,
    )

    adjusted_confidence = (
        original_confidence
        + confidence
    )

    adjusted_confidence = max(
        0,
        min(
            adjusted_confidence,
            100,
        ),
    )

    return {
        **decision,
        "learning_confidence": adjusted_confidence,
    }


def generate_adaptive_coaching_response(
    decision: dict,
) -> dict:
    """
    Convert decision into athlete
    friendly coaching response.
    """

    action = decision.get(
        "action",
        "",
    )

    explanation = decision.get(
        "explanation",
        "",
    )

    return {
        "decision": decision.get(
            "decision",
            "",
        ),
        "action": action,
        "confidence": decision.get(
            "learning_confidence",
            50,
        ),
        "message": (
            f"{action} "
            f"{explanation}"
        ),
    }


def run_adaptive_coaching_engine(
    coach_context: dict,
    learning_memory: dict | None = None,
) -> dict:
    """
    Complete adaptive coaching pipeline.

    Flow:
    Context
      ↓
    Decision
      ↓
    Learning adjustment
      ↓
    Athlete response
    """

    if learning_memory is None:
        learning_memory = {}

    decision = build_adaptive_training_decision(
        coach_context,
    )

    decision = apply_learning_adjustment(
        decision,
        learning_memory,
    )

    return generate_adaptive_coaching_response(
        decision,
    )
