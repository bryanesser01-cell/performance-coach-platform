def evaluate_training_state(
    readiness_score: int,
    training_stress: int,
    fitness_trend: str,
    learning_confidence: int = 50,
) -> dict:
    """
    Evaluate athlete training state.

    Inputs:
    - Recovery readiness
    - Training stress
    - Fitness trend
    - Previous coaching confidence

    Returns:
    - Training recommendation state
    """

    if readiness_score < 40:

        decision = "REDUCE_TRAINING"

        reason = (
            "Recovery status indicates "
            "the athlete needs more recovery."
        )

    elif training_stress >= 500:

        decision = "REDUCE_TRAINING"

        reason = (
            "Training load is high and "
            "fatigue risk is increasing."
        )

    elif (
        fitness_trend == "improving"
        and readiness_score >= 70
    ):

        decision = "PROGRESS_TRAINING"

        reason = (
            "Fitness is improving and "
            "the athlete is ready to progress."
        )

    else:

        decision = "MAINTAIN_TRAINING"

        reason = (
            "Current training balance "
            "should be maintained."
        )

    return {
        "decision": decision,
        "reason": reason,
        "learning_confidence": learning_confidence,
    }


def select_coach_action(
    training_state: dict,
) -> dict:
    """
    Convert decision into athlete action.
    """

    decision = training_state.get(
        "decision",
        "MAINTAIN_TRAINING",
    )

    actions = {
        "REDUCE_TRAINING": (
            "Complete an easy session "
            "or take a recovery day."
        ),
        "PROGRESS_TRAINING": (
            "Increase training stimulus "
            "gradually."
        ),
        "MAINTAIN_TRAINING": (
            "Continue current training plan."
        ),
    }

    return {
        "decision": decision,
        "action": actions.get(
            decision,
            actions["MAINTAIN_TRAINING"],
        ),
    }


def generate_decision_explanation(
    decision_context: dict,
) -> dict:
    """
    Create athlete-friendly explanation.
    """

    decision = decision_context.get(
        "decision",
        "",
    )

    reason = decision_context.get(
        "reason",
        "",
    )

    return {
        "decision": decision,
        "explanation": (
            f"The coach selected {decision} "
            f" because {reason}"
        ),
    }


def generate_coach_decision(
    readiness_score: int,
    training_stress: int,
    fitness_trend: str,
    learning_confidence: int = 50,
) -> dict:
    """
    Complete AI Coach decision pipeline.
    """

    state = evaluate_training_state(
        readiness_score=readiness_score,
        training_stress=training_stress,
        fitness_trend=fitness_trend,
        learning_confidence=learning_confidence,
    )

    action = select_coach_action(
        state,
    )

    explanation = generate_decision_explanation(
        state,
    )

    return {
        **state,
        **action,
        **explanation,
    }
