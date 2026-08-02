"""
Coach Context

Shared context object passed between AI Coach services.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class CoachContext:
    """
    Shared AI Coach context.

    This object contains all information gathered by the
    orchestrator before the Coach Brain generates a decision.
    """

    #
    # Identity
    #
    athlete_id: int

    #
    # Athlete
    #
    athlete_state: dict = field(
        default_factory=dict,
    )

    #
    # Memory
    #
    memory_context: dict = field(
        default_factory=dict,
    )

    memory_reasoning: dict = field(
        default_factory=dict,
    )

    #
    # Intelligence
    #
    goal_intelligence: dict = field(
        default_factory=dict,
    )

    performance_intelligence: dict = field(
        default_factory=dict,
    )

    performance_prediction: dict = field(
        default_factory=dict,
    )

    recovery_intelligence: dict = field(
        default_factory=dict,
    )

    training_load_intelligence: dict = field(
        default_factory=dict,
    )

    race_intelligence: dict = field(
        default_factory=dict,
    )

    periodisation: dict = field(
        default_factory=dict,
    )

    #
    # Decision
    #
    decision: dict = field(
        default_factory=dict,
    )

    decision_scoring: dict = field(
        default_factory=dict,
    )

    confidence: dict = field(
        default_factory=dict,
    )

    coach_brain: dict = field(
        default_factory=dict,
    )

    training_plan: dict = field(
        default_factory=dict,
    )

    coach_response: dict = field(
        default_factory=dict,
    )

    #
    # Metadata
    #
    metadata: dict = field(
        default_factory=dict,
    )
