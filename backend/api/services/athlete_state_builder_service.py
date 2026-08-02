"""
Athlete State Builder Service

Creates the state object used by
the adaptive coaching engine.
"""


def build_athlete_state(
    readiness: dict,
    training: dict,
    performance: dict,
    memory_context: dict | None = None,
) -> dict:
    """
    Build adaptive coaching state.
    """

    return {
        "readiness": readiness,
        "training": training,
        "performance": performance,
        "memory": memory_context or {},
        "state_ready": True,
    }
