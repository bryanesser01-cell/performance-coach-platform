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
from api.services.coach_brain_service import (
    CoachBrainService,
)


def run_ai_coach_orchestrator(
    db: Session,
    athlete_id: int,
) -> dict:
    """
    Main AI Coach Orchestrator.

    Flow

        Athlete State
              ↓
        Memory Context
              ↓
        Memory Reasoning
              ↓
        Adaptive Decision
              ↓
        Coach Brain
              ↓
        API Response
    """

    # Build athlete state
    athlete_state = get_athlete_state(
        db,
        athlete_id,
    )

    # Load memory context
    memory_context = MemoryContextService(
        db
    ).build_context(
        athlete_id,
    )

    # Analyse memory
    memory_reasoning = (
        MemoryReasoningService().analyse(
            memory_context,
        )
    )

    # Generate coaching decision
    decision = generate_adaptive_coach_decision(
        athlete_id=athlete_id,
        athlete_state=athlete_state,
        memory_context=memory_context,
    )

    # Build final coach brain output
    coach_brain = CoachBrainService().build_decision(
        athlete_state=athlete_state,
        memory_reasoning=memory_reasoning,
        decision=decision,
    )

    return {
        "athlete_id": athlete_id,
        "athlete_state": athlete_state,
        "memory_context": memory_context,
        "memory_reasoning": memory_reasoning,
        "decision": decision,
        "coach_brain": coach_brain,
        "coach_message": coach_brain["summary"],
        "ai_coach": True,
    }
