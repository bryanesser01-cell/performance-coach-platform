from api.services.coach_learning_memory_service import (
    calculate_decision_confidence,
)


def generate_learning_aware_decision(
    athlete_id: int,
    proposed_decision: str,
) -> dict:
    """
    Adjust coaching decision confidence
    using previous learning history.

    Flow:

    Proposed Decision
          |
          ↓
    Learning Memory
          |
          ↓
    Confidence Score
          |
          ↓
    Learning-aware Recommendation
    """

    confidence = calculate_decision_confidence(
        athlete_id=athlete_id,
        decision=proposed_decision,
    )

    if confidence >= 70:

        reason = "Previous athlete outcomes " "support this decision."

    elif confidence <= 40:

        reason = "Previous outcomes suggest " "reviewing this decision."

    else:

        reason = (
            "Limited learning history available. "
            "Continue monitoring athlete response."
        )

    return {
        "athlete_id": athlete_id,
        "proposed_decision": proposed_decision,
        "recommended_decision": proposed_decision,
        "confidence": confidence,
        "reason": reason,
    }


def build_learning_aware_context(
    athlete_id: int,
    decision: str,
) -> dict:
    """
    Build context for AI Coach decisions.
    """

    decision_context = generate_learning_aware_decision(
        athlete_id=athlete_id,
        proposed_decision=decision,
    )

    return {
        "learning_aware_decision": decision_context,
    }
