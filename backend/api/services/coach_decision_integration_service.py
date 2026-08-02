from api.services.coach_decision_explanation_service import (
    explain_coach_decision,
)


def generate_coach_decision(
    athlete_state: dict,
) -> dict:
    """
    Legacy compatibility interface.

    Preserves original decision behaviour.

    Returns:
    - progress_training
    - recover
    - reduce_load
    - maintain_training
    """

    readiness = athlete_state.get(
        "readiness",
        {},
    )

    training = athlete_state.get(
        "training",
        {},
    )

    performance = athlete_state.get(
        "performance",
        {},
    )

    readiness_score = readiness.get(
        "score",
        0,
    )

    training_load = training.get(
        "load_status",
        "unknown",
    )

    performance_trend = performance.get(
        "trend",
        "unknown",
    )

    if (
        readiness_score >= 80
        and training_load == "optimal"
        and performance_trend == "improving"
    ):
        return {
            "decision": "progress_training",
            "priority": "quality_session",
            "reason": (
                "Athlete readiness is high, "
                "training load is appropriate, "
                "and performance is improving."
            ),
        }

    if readiness_score < 60:
        return {
            "decision": "recover",
            "priority": "recovery",
            "reason": ("Readiness is low. " "Recovery is recommended."),
        }

    if training_load == "high":
        return {
            "decision": "reduce_load",
            "priority": "easy_session",
            "reason": ("Training load is elevated. " "Reduce intensity."),
        }

    return {
        "decision": "maintain_training",
        "priority": "normal_session",
        "reason": ("Maintain current training approach " "and continue monitoring."),
    }


def generate_coach_decision_context(
    athlete_state: dict,
) -> dict:
    """
    AI Coach integration interface.

    Uses adaptive decision terminology:

    - PROGRESS_TRAINING
    - REDUCE_TRAINING
    - MAINTAIN_TRAINING
    """

    readiness = athlete_state.get(
        "readiness",
        {},
    )

    training = athlete_state.get(
        "training",
        {},
    )

    performance = athlete_state.get(
        "performance",
        {},
    )

    readiness_score = readiness.get(
        "score",
        0,
    )

    training_load = training.get(
        "load_status",
        "unknown",
    )

    performance_trend = performance.get(
        "trend",
        "unknown",
    )

    if (
        readiness_score >= 80
        and training_load == "optimal"
        and performance_trend == "improving"
    ):
        decision = {
            "decision": "PROGRESS_TRAINING",
            "priority": "quality_session",
            "reason": (
                "Athlete readiness is high, "
                "training load is appropriate, "
                "and performance is improving."
            ),
        }

    elif readiness_score < 60:

        decision = {
            "decision": "REDUCE_TRAINING",
            "priority": "recovery",
            "reason": ("Readiness is low and recovery " "requires attention."),
        }

    elif training_load == "high":

        decision = {
            "decision": "REDUCE_TRAINING",
            "priority": "easy_session",
            "reason": ("Training load is elevated. " "Reduce intensity."),
        }

    else:

        decision = {
            "decision": "MAINTAIN_TRAINING",
            "priority": "normal_session",
            "reason": ("Training load and performance " "are currently balanced."),
        }

    explanation = explain_coach_decision(
        decision=decision.get(
            "decision",
            "",
        ),
        reason=decision.get(
            "reason",
            "",
        ),
    )

    return {
        "athlete_state": athlete_state,
        "coach_decision": decision,
        "decision_explanation": explanation,
    }


def build_coach_decision_context(
    athlete_state: dict,
) -> dict:
    """
    Backwards compatible wrapper.
    """

    return generate_coach_decision_context(
        athlete_state,
    )
