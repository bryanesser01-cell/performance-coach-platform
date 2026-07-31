from sqlalchemy.orm import Session

from api.services.adaptive_coach_decision_service import (
    generate_adaptive_coach_decision,
)
from api.services.athlete_state_service import (
    get_athlete_state,
)


def run_ai_coach_orchestrator(
    db: Session,
    athlete_id: int,
) -> dict:
    """
    Main AI Coach decision orchestrator.

    Flow:

    Athlete State
        ↓
    Adaptive Decision
        ↓
    Coach Response
    """

    athlete_state = get_athlete_state(
        db,
        athlete_id,
    )

    decision = generate_adaptive_coach_decision(
        athlete_id,
        athlete_state,
    )

    return {
        "athlete_id": athlete_id,

        "athlete_state": athlete_state,

        "decision": decision,

        "coach_message": (
            f"Recommended action: "
            f"{decision.get('recommendation')}"
        ),

        "ai_coach": True,
    }
