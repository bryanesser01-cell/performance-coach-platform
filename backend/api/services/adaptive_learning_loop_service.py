from api.services.coach_decision_learning_hook_service import (
    process_coach_outcome,
)
from api.services.coach_decision_record_service import (
    record_coach_decision,
)
from api.services.training_session_analysis_service import (
    analyse_training_outcome,
)


def record_adaptive_coaching_decision(
    db,
    athlete_id: int,
    decision: dict,
) -> dict:
    """
    Store adaptive coaching decision.
    """

    return record_coach_decision(
        db=db,
        athlete_id=athlete_id,
        decision=decision.get(
            "decision",
        ),
        reason=decision.get(
            "reason",
        ),
        confidence=decision.get(
            "learning_confidence",
            0,
        ),
    )


def process_adaptive_workout_outcome(
    db,
    athlete_id: int,
    decision: str,
    workout_result: dict,
) -> dict:
    """
    Process athlete response after workout.
    """

    analysis = analyse_training_outcome(
        workout_result,
    )

    learning = process_coach_outcome(
        db=db,
        athlete_id=athlete_id,
        decision=decision,
        outcome=analysis.get(
            "outcome",
        ),
    )

    return {
        "athlete_id": athlete_id,
        "decision": decision,
        "workout_analysis": analysis,
        "learning_update": learning,
        "learning_recorded": True,
    }
