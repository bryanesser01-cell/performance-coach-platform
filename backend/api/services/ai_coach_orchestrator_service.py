from sqlalchemy.orm import Session

from api.models.coach_context import CoachContext
from api.services.coach_pipeline import (
    CoachPipeline,
)
from api.services.pipeline_steps.adaptive_decision_step import (
    AdaptiveDecisionStep,
)
from api.services.pipeline_steps.athlete_state_step import (
    AthleteStateStep,
)
from api.services.pipeline_steps.coach_brain_step import (
    CoachBrainStep,
)
from api.services.pipeline_steps.confidence_step import (
    ConfidenceStep,
)
from api.services.pipeline_steps.decision_rules_step import (
    DecisionRulesStep,
)
from api.services.pipeline_steps.decision_scoring_step import (
    DecisionScoringStep,
)
from api.services.pipeline_steps.goal_intelligence_step import (
    GoalIntelligenceStep,
)
from api.services.pipeline_steps.memory_context_step import (
    MemoryContextStep,
)
from api.services.pipeline_steps.memory_reasoning_step import (
    MemoryReasoningStep,
)
from api.services.pipeline_steps.performance_intelligence_step import (
    PerformanceIntelligenceStep,
)
from api.services.pipeline_steps.periodisation_step import (
    PeriodisationStep,
)
from api.services.pipeline_steps.race_intelligence_step import (
    RaceIntelligenceStep,
)
from api.services.pipeline_steps.recovery_intelligence_step import (
    RecoveryIntelligenceStep,
)
from api.services.pipeline_steps.training_load_intelligence_step import (
    TrainingLoadIntelligenceStep,
)
from api.services.pipeline_steps.training_plan_step import (
    TrainingPlanStep,
)


def run_ai_coach_orchestrator(
    db: Session,
    athlete_id: int,
) -> dict:
    """
    Main AI Coach Orchestrator.
    """

    #
    # Create shared coach context
    #
    context = CoachContext(
        athlete_id=athlete_id,
    )

    #
    # Build Coach Pipeline
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

    pipeline.add_step(
        RaceIntelligenceStep(),
    )

    pipeline.add_step(
        PeriodisationStep(),
    )

    pipeline.add_step(
        DecisionRulesStep(),
    )

    pipeline.add_step(
        DecisionScoringStep(),
    )

    pipeline.add_step(
        ConfidenceStep(),
    )

    pipeline.add_step(
        AdaptiveDecisionStep(),
    )

    pipeline.add_step(
        CoachBrainStep(),
    )

    #
    # NEW
    #
    pipeline.add_step(
        TrainingPlanStep(),
    )

    #
    # Execute pipeline
    #
    pipeline.run(
        context,
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
        "performance_intelligence": (context.performance_intelligence),
        "recovery_intelligence": (context.recovery_intelligence),
        "training_load_intelligence": (context.training_load_intelligence),
        "race_intelligence": (context.race_intelligence),
        "periodisation": (context.periodisation),
        "decision": context.decision,
        "decision_scoring": (context.decision_scoring),
        "confidence": context.confidence,
        "coach_brain": context.coach_brain,
        "training_plan": (context.training_plan),
        "coach_message": (
            context.coach_brain.get(
                "summary",
                "",
            )
        ),
        "ai_coach": True,
    }
