from api.services.coach_context_engine_service import (
    build_coach_context,
)


def build_athlete_context(
    athlete_id: int,
    athlete_profile: dict,
    training_state: dict,
    memories: list[str] | None = None,
    days_to_race: int | None = None,
) -> dict:
    """
    Build complete athlete context.

    Combines:
    - Athlete profile
    - Training state
    - Memory
    - Race timeline
    - Coach decision context
    """

    context = build_coach_context(
        athlete_id=athlete_id,
        goal=athlete_profile.get(
            "goal",
            "Improve performance",
        ),
        readiness_score=training_state.get(
            "readiness_score",
            0,
        ),
        training_load_status=training_state.get(
            "training_load_status",
            "unknown",
        ),
        performance_trend=training_state.get(
            "performance_trend",
            "unknown",
        ),
        memories=memories,
        days_to_race=days_to_race,
    )

    return {
        "athlete": {
            "id": athlete_id,
            "name": athlete_profile.get(
                "name",
            ),
            "sport": athlete_profile.get(
                "sport",
                "running",
            ),
            "primary_event": athlete_profile.get(
                "primary_event",
                "5K",
            ),
        },
        "goal": context["goal"],
        "training": {
            "readiness_score": context["readiness_score"],
            "training_load_status": context["training_load_status"],
            "performance_trend": context["performance_trend"],
        },
        "memories": context["memories"],
        "decision": context["decision"],
    }


def generate_context_summary(
    athlete_context: dict,
) -> str:
    """
    Generate AI coach context summary.
    """

    decision = athlete_context["decision"]

    return (
        f"{athlete_context['athlete']['name']} "
        f"is training for "
        f"{athlete_context['goal']}. "
        f"Readiness is "
        f"{athlete_context['training']['readiness_score']}. "
        f"Recommendation: "
        f"{decision['recommendation']}"
    )
