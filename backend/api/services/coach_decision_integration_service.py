def generate_coach_decision(
    athlete_state: dict,
) -> dict:
    """
    Generate coaching decision from athlete state.

    Uses:
    - Readiness
    - Training load
    - Performance trend
    - Goal
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
            "reason": (
                "Readiness is low. "
                "Recovery is recommended."
            ),
        }

    if training_load == "high":
        return {
            "decision": "reduce_load",
            "priority": "easy_session",
            "reason": (
                "Training load is elevated. "
                "Reduce intensity."
            ),
        }

    return {
        "decision": "maintain_training",
        "priority": "normal_session",
        "reason": (
            "Maintain current training approach "
            "and continue monitoring."
        ),
    }


def build_coach_decision_context(
    athlete_state: dict,
) -> dict:
    """
    Prepare athlete state for AI coach.
    """

    decision = generate_coach_decision(
        athlete_state,
    )

    return {
        "athlete_state": athlete_state,
        "coach_decision": decision,
    }
