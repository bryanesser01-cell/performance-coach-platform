"""
Athlete Intelligence Memory Service

Combines:
- athlete memories
- performance memory
- coach learning
"""

from api.services.athlete_memory_service import (
    build_memory_context,
)
from api.services.coach_learning_service import (
    identify_training_patterns,
)
from api.services.performance_memory_service import (
    build_performance_memory,
)


def build_athlete_intelligence_memory(
    athlete_profile: dict,
    stored_memories: list,
    race_results: list[dict],
    training_history: list[dict],
) -> dict:
    """
    Build complete athlete intelligence memory.
    """

    memory_context = build_memory_context(
        stored_memories,
    )

    performance_memory = (
        build_performance_memory(
            athlete_profile,
            race_results,
            training_history,
        )
    )

    learning_patterns = (
        identify_training_patterns(
            training_history,
        )
    )

    return {
        "athlete_profile": athlete_profile,

        "memory_context": memory_context,

        "performance_memory": performance_memory,

        "training_patterns": learning_patterns,

        "intelligence_ready": True,
    }


def generate_memory_intelligence_insight(
    intelligence_memory: dict,
) -> dict:
    """
    Generate AI coaching insight from memory.
    """

    patterns = intelligence_memory.get(
        "training_patterns",
        {},
    )

    return {
        "strengths": patterns.get(
            "responds_well_to",
            [],
        ),

        "challenges": patterns.get(
            "struggles_with",
            [],
        ),

        "coach_message": (
            "Future coaching decisions "
            "will adapt using athlete "
            "history and response patterns."
        ),
    }
