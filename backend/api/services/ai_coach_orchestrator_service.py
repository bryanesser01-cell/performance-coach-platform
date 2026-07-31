from sqlalchemy.orm import Session

from api.models.coach_context import CoachContext

from api.services.adaptive_coach_decision_service import (
    generate_adaptive_coach_decision,
)
from api.services.athlete_state_service import (
    get_athlete_state,
)
from api.services.coach_brain_service import (
    CoachBrainService,
)
from api.services.goal_intelligence_service import (
    GoalIntelligenceService,
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
    Main AI Coach Orchestrator.

    Flow

        Athlete State
              ↓
        Memory Context
              ↓
        Memory Reasoning
              ↓
        Goal Intelligence
              ↓
        Adaptive Decision
              ↓
        Coach Brain
              ↓
        API Response
    """

    #
    # Create shared coach context
    #
    context = CoachContext(
        athlete_id=athlete_id,
    )

    #
    # Athlete State
    #
    context.athlete_state = get_athlete_state(
        db,
        athlete_id,
    )

    #
    # Memory Context
    #
    context.memory_context = (
        MemoryContextService(db)
        .build_context(
            athlete_id,
        )
    )

    #
    # Memory Reasoning
    #
    context.memory_reasoning = (
        MemoryReasoningService()
        .analyse(
            context.memory_context,
        )
    )

    #
    # Goal Intelligence
    #
    context.goal_intelligence = (
        GoalIntelligenceService()
        .analyse(
            context.athlete_state,
        )
    )

    #
    # Adaptive Decision
    #
    # Keep using the legacy API for now so existing
    # tests and callers continue to work.
    #
    context.decision = (
        generate_adaptive_coach_decision(
            athlete_id=context.athlete_id,
            athlete_state=context.athlete_state,
            memory_context=context.memory_context,
        )
    )

    #
    # Coach Brain
    #
    CoachBrainService().build_decision(
        context=context,
    )

    #
    # API Response
    #
    return {
        "athlete_id": context.athlete_id,
        "athlete_state": context.athlete_state,
        "memory_context": context.memory_context,
        "memory_reasoning": context.memory_reasoning,
        "goal_intelligence": context.goal_intelligence,
        "decision": context.decision,
        "coach_brain": context.coach_brain,
        "coach_message": context.coach_brain["summary"],
        "ai_coach": True,
    }
