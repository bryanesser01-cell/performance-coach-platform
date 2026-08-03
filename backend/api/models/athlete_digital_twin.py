from __future__ import annotations

from dataclasses import (
    dataclass,
    field,
)


@dataclass
class AthleteDigitalTwin:
    """
    Complete AI representation of an athlete.

    This object becomes the single source of truth
    used by the AI Coach.

    Every intelligence service contributes data to
    this model.

    Future versions will also include:

    - physiology
    - biomechanics
    - nutrition
    - sleep
    - psychology
    - wearable metrics
    """

    #
    # Athlete
    #
    athlete: dict = field(
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

    recovery_intelligence: dict = field(
        default_factory=dict,
    )

    training_load_intelligence: dict = field(
        default_factory=dict,
    )

    race_intelligence: dict = field(
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
    # Coach
    #
    decision_history: list = field(
        default_factory=list,
    )

    metadata: dict = field(
        default_factory=dict,
    )
