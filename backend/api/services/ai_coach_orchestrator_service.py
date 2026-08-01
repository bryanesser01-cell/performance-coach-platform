from sqlalchemy.orm import Session

from api.models.coach_context import CoachContext

from api.services.coach_pipeline import (
    CoachPipeline,
)

from api.services.pipeline_steps.athlete_state_step import (
    AthleteStateStep,
)
from api.services.pipeline_steps.memory_context_step import (
    MemoryContextStep,
)
from api.services.pipeline_steps.memory_reasoning_step import (
    MemoryReasoningStep,
)
from api.services.pipeline_steps.goal_intelligence_step import (
    GoalIntelligenceStep,
)
from api.services.pipeline_steps.performance_intelligence_step import (
    PerformanceIntelligenceStep,
)
from api.services.pipeline_steps.recovery_intelligence_step import (
    RecoveryIntelligenceStep,
)
from api.services.pipeline_steps.training_load_intelligence_step import (
    TrainingLoadIntelligenceStep,
)

from api.services.adaptive_coach_decision_service import (
    generate_adaptive_coach_decision,
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
        Goal Intelligence
              ↓
        Performance Intelligence
              ↓
        Recovery Intelligence
              ↓
        Training Load Intelligence
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
    # Pipeline
    #
    pipeline = CoachPipeline()

    pipeline.add_step(
        AthleteStateStep(db),
    )

    pipeline.add_step(
        MemoryContextStep(db),
    )

    pipeline.add_step(
        MemoryReasoningStep(),
    )

    pipeline.add_step(
        GoalIntelligenceStep(),
    )

    pipeline.add_step(
        PerformanceIntelligenceStep(),
    )

    pipeline.add_step(
        RecoveryIntelligenceStep(),
    )

    pipeline.add_step(
        TrainingLoadIntelligenceStep(),
    )

    pipeline.run(
        context,
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
        "performance_intelligence": (
            context.performance_intelligence
        ),
        "recovery_intelligence": (
            context.recovery_intelligence
        ),
        "training_load_intelligence": (
            context.training_load_intelligence
        ),
        "decision": context.decision,
        "coach_brain": context.coach_brain,
        "coach_message": context.coach_brain["summary"],
        "ai_coach": True,
    }
