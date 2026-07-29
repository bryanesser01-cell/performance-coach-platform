def analyse_coach_decision_outcome(
    decision: str,
    completed: bool,
    athlete_rpe: int | None = None,
    fatigue_after: str | None = None,
) -> dict:
    """
    Analyse the outcome of a coaching decision.

    Produces a learning signal that can be
    used to improve future decisions.
    """

    learning_signal = "neutral"

    confidence_update = 0

    if not completed:

        return {
            "learning_signal": "negative",
            "confidence_update": -1,
            "reason": (
                "Workout was not completed."
            ),
        }

    if (
        fatigue_after == "low"
        and athlete_rpe is not None
        and athlete_rpe <= 5
    ):
        learning_signal = "positive"
        confidence_update = 1

    elif (
        fatigue_after == "high"
        and athlete_rpe is not None
        and athlete_rpe >= 8
    ):
        learning_signal = "negative"
        confidence_update = -1

    return {
        "decision": decision,
        "completed": completed,
        "athlete_rpe": athlete_rpe,
        "fatigue_after": fatigue_after,
        "learning_signal": learning_signal,
        "confidence_update": confidence_update,
    }


def build_learning_context(
    decision: str,
    outcome: dict,
) -> dict:
    """
    Build learning context for AI Coach.
    """

    return {
        "decision": decision,
        "outcome": outcome,
        "coach_learning": {
            "signal": (
                outcome.get(
                    "learning_signal",
                    "neutral",
                )
            ),
            "confidence_update": (
                outcome.get(
                    "confidence_update",
                    0,
                )
            ),
        },
    }
