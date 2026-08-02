def build_athlete_strategy_profile(
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
) -> dict:
    """
    Build personalised athlete strategy profile.

    Combines:
    - Athlete characteristics
    - Training history
    - Recovery patterns
    - Decision success history
    """

    preferred_strategy = "BALANCED_TRAINING"

    confidence = 50

    reason = "Insufficient history available. " "Using balanced approach."

    recovery_success = decision_analysis.get(
        "REDUCE_TRAINING",
        {},
    ).get(
        "success_rate",
        0,
    )

    progression_success = decision_analysis.get(
        "PROGRESS_TRAINING",
        {},
    ).get(
        "success_rate",
        0,
    )

    if recovery_success > progression_success:

        preferred_strategy = "RECOVERY_FIRST"

        confidence = recovery_success

        reason = "Athlete historically responds " "better when recovery is prioritised."

    elif progression_success > recovery_success:

        preferred_strategy = "PROGRESSION_FOCUSED"

        confidence = progression_success

        reason = "Athlete historically responds " "well to progressive training."

    return {
        "preferred_strategy": preferred_strategy,
        "confidence": confidence,
        "reason": reason,
        "training_sessions": len(
            training_history,
        ),
        "recovery_sessions": len(
            recovery_history,
        ),
    }


def select_personalised_training_strategy(
    athlete_strategy_profile: dict,
    current_state: dict,
) -> dict:
    """
    Select strategy based on athlete profile
    and current condition.
    """

    preferred_strategy = athlete_strategy_profile.get(
        "preferred_strategy",
        "BALANCED_TRAINING",
    )

    readiness = current_state.get(
        "readiness_score",
        50,
    )

    if readiness < 40:

        recommendation = "RECOVERY_FIRST"

    else:

        recommendation = preferred_strategy

    return {
        "strategy": recommendation,
        "confidence": athlete_strategy_profile.get(
            "confidence",
            50,
        ),
    }


def generate_strategy_recommendation(
    athlete_id: int,
    strategy_result: dict,
) -> dict:
    """
    Generate final athlete strategy output.
    """

    return {
        "athlete_id": athlete_id,
        "recommended_strategy": strategy_result.get(
            "strategy",
            "BALANCED_TRAINING",
        ),
        "confidence": strategy_result.get(
            "confidence",
            50,
        ),
        "message": (
            "Training strategy personalised " "from your historical responses."
        ),
    }


def run_athlete_strategy_engine(
    athlete_id: int,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Complete personalised strategy pipeline.
    """

    profile = build_athlete_strategy_profile(
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
    )

    strategy = select_personalised_training_strategy(
        athlete_strategy_profile=profile,
        current_state=current_state,
    )

    return generate_strategy_recommendation(
        athlete_id=athlete_id,
        strategy_result=strategy,
    )
