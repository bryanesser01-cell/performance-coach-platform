from sqlalchemy.orm import Session

from api.services.adaptive_coach_decision_service import (
    generate_adaptive_coach_decision,
)
from api.services.athlete_state_service import (
    get_athlete_state,
)
from api.services.memory_context_service import (
    MemoryContextService,
)
from api.services.memory_reasoning_service import (
    MemoryReasoningService,
)


def run_ai_coach_orchestrator(
    db: Session,
    athlete_id: int,
) -> dict:
    """
    Main AI Coach decision orchestrator.

    Flow

    Athlete State
          ↓
    Memory Context
          ↓
    Memory Reasoning
          ↓
    Adaptive Decision
          ↓
    Coach Response
    """

    athlete_state = get_athlete_state(
        db,
        athlete_id,
    )

    memory_context = MemoryContextService(db).build_context(
        athlete_id,
    )

    memory_reasoning = (
        MemoryReasoningService().analyse(
            memory_context,
        )
    )

    decision = generate_adaptive_coach_decision(
        athlete_id=athlete_id,
        athlete_state=athlete_state,
        memory_context=memory_context,
    )

    return {
        "athlete_id": athlete_id,
        "athlete_state": athlete_state,
        "memory_context": memory_context,
        "memory_reasoning": memory_reasoning,
        "decision": decision,
        "coach_message": (
            f"Recommended action: "
            f"{decision.get('recommendation')}"
        ),
        "ai_coach": True,
    }
