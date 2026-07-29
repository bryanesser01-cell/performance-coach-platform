from api.services.coach_learning_service import (
    analyse_coach_decision_outcome,
)


def process_coach_learning_update(
    decision: str,
    completed: bool,
    athlete_rpe: int | None = None,
    fatigue_after: str | None = None,
) -> dict:
    """
    Connects coach decisions with learning outcomes.

    Flow:

    Decision
        ↓
    Outcome Analysis
        ↓
    Learning Update
    """

    outcome = analyse_coach_decision_outcome(
        decision=decision,
        completed=completed,
        athlete_rpe=athlete_rpe,
        fatigue_after=fatigue_after,
    )

    learning_signal = outcome.get(
        "learning_signal",
        "neutral",
    )

    if learning_signal == "positive":

        message = (
            "Decision supported by athlete outcome."
        )

    elif learning_signal == "negative":

        message = (
            "Decision should be reviewed "
            "using future athlete responses."
        )

    else:

        message = (
            "More athlete data is required "
            "to improve confidence."
        )

    return {
        "decision": decision,
        "outcome": outcome,
        "learning_update": {
            "signal": learning_signal,
            "confidence_update": (
                outcome.get(
                    "confidence_update",
                    0,
                )
            ),
            "message": message,
        },
    }
