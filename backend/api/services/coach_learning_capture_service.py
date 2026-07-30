"""
Coach Learning Capture Service

Stores coaching outcomes and athlete feedback.
"""


def record_learning_event(
    event: dict,
) -> dict:
    """
    Database placeholder.
    """

    return {
        "id": 1,
        **event,
    }



def calculate_learning_update(
    signal: str,
) -> int:
    """
    Convert signal into confidence change.
    """

    if signal == "positive":
        return 10

    if signal == "negative":
        return -10

    return 0



def capture_coach_decision_outcome(
    db,
    athlete_id: int,
    decision: str,
    outcome: str,
) -> dict:
    """
    Capture coach decision outcome.
    """

    confidence_change = (
        calculate_learning_update(
            outcome
        )
    )


    return {
        **record_learning_event(
            {
                "athlete_id": athlete_id,
                "decision": decision,
            }
        ),

        "outcome": outcome,

        "confidence_change": confidence_change,
    }
    """
    Capture coach decision outcome.
    """

    confidence_change = (
        calculate_learning_update(
            outcome
        )
    )


    return {
        **record_learning_event(
            {
                "athlete_id": athlete_id,
                "decision": decision,
                "outcome": outcome,
            }
        ),

        "confidence_change": confidence_change,
    }



def store_learning_feedback(
    db,
    athlete_id: int,
    decision: str,
    completed: bool,
    performance_change: str,
) -> dict:
    """
    Store athlete feedback.

    Converts performance change
    into learning outcome.
    """

    if performance_change in [
        "improved",
        "better",
        "successful",
    ]:

        outcome = "positive"


    elif performance_change in [
        "declined",
        "worse",
        "poor",
    ]:

        outcome = "negative"


    else:

        outcome = (
            "positive"
            if completed
            else "negative"
        )


    return {
        **record_learning_event(
            {
                "athlete_id": athlete_id,
                "decision": decision,
                "completed": completed,
                "performance_change": performance_change,
            }
        ),

        "outcome": outcome,
    }
