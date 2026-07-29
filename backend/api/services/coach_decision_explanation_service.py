def explain_coach_decision(
    decision: str,
    reason: str,
    execution_score: int | None = None,
    fatigue_signal: str | None = None,
) -> dict:
    """
    Convert adaptive coaching decisions
    into athlete-friendly explanations.
    """

    if decision == "REDUCE_TRAINING":

        message = (
            "I have reduced your training load "
            "because your recent workout showed "
            "signs that your body needs more recovery."
        )

    elif decision == "PROGRESS_TRAINING":

        message = (
            "Your training is progressing because "
            "you are completing workouts well and "
            "showing positive fitness signs."
        )

    elif decision == "RACE_TAPER":

        message = (
            "Your training has been reduced because "
            "your race is approaching. The focus is "
            "now on freshness and performance."
        )

    elif decision == "MAINTAIN_TRAINING":

        message = (
            "Your current training is working well, "
            "so we will maintain the plan and continue "
            "building consistency."
        )

    else:

        message = (
            "Your training has been adjusted based "
            "on your current recovery and performance."
        )

    if fatigue_signal == "high":

        message += (
            " Your recent feedback showed high fatigue, "
            "so recovery is the priority."
        )

    if execution_score is not None:

        message += (
            f" Your workout execution score was "
            f"{execution_score}/100."
        )

    return {
        "decision": decision,
        "reason": reason,
        "athlete_message": message,
    }


def build_short_coach_explanation(
    explanation: dict,
) -> str:
    """
    Return simple coach message.
    """

    return explanation.get(
        "athlete_message",
        "Training decision updated.",
    )
