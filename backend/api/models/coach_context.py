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

    athlete_id: int

    athlete_state: dict = field(default_factory=dict)

    memory_context: dict = field(default_factory=dict)

    memory_reasoning: dict = field(default_factory=dict)

    goal_intelligence: dict = field(default_factory=dict)

    performance_intelligence: dict = field(default_factory=dict)

    performance_prediction: dict = field(default_factory=dict)

    recovery_intelligence: dict = field(default_factory=dict)

    decision: dict = field(default_factory=dict)

    coach_brain: dict = field(default_factory=dict)

    metadata: dict = field(default_factory=dict)
