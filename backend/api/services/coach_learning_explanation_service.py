def build_learning_explanation(
    decision: str,
    confidence: int,
    reason: str | None = None,
    learning_history: dict | None = None,
) -> dict:
    """
    Build a human-readable explanation
    for an AI Coach decision.

    Uses:
    - Decision
    - Confidence score
    - Previous learning context
    """

    if decision == "REDUCE_TRAINING":

        action = "I reduced your training load " "to prioritise recovery."

    elif decision == "PROGRESS_TRAINING":

        action = (
            "I increased your training "
            "because your indicators support "
            "further progression."
        )

    elif decision == "RACE_TAPER":

        action = "I adjusted your training to " "prioritise freshness before your race."

    else:

        action = "I adjusted your training " "based on your current indicators."

    if reason:

        explanation = f"{action} {reason}"

    else:

        explanation = action

    if learning_history:

        explanation += (
            " Previous athlete outcomes "
            "have been considered when "
            "making this recommendation."
        )

    return {
        "decision": decision,
        "confidence": confidence,
        "explanation": explanation,
    }


def build_athlete_friendly_message(
    explanation: dict,
) -> str:
    """
    Convert decision explanation into
    a coach-style athlete message.
    """

    confidence = explanation.get(
        "confidence",
        0,
    )

    message = explanation.get(
        "explanation",
        "",
    )

    return f"{message} " f"My confidence in this decision " f"is {confidence}%."
