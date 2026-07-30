from api.services.activity_coach_integration_service import (
    build_activity_coach_context,
    detect_training_risk,
    generate_activity_based_recommendation,
)


def build_activity_memory_context(
    activities: list[dict],
) -> dict:
    """
    Build activity intelligence context
    for AI Coach memory.

    Combines:
    - Activity history
    - Training stress
    - Fitness trend
    - Training risk
    - Recommendation
    """

    activity_context = build_activity_coach_context(
        activities,
    )

    risk = detect_training_risk(
        activity_context,
    )

    recommendation = generate_activity_based_recommendation(
        activity_context,
    )

    return {
        "activity_context": activity_context,
        "training_risk": risk,
        "recommendation": recommendation,
    }


def enrich_coach_memory_with_activity(
    memory_context: dict,
    activities: list[dict],
) -> dict:
    """
    Add activity intelligence into
    existing coach memory context.
    """

    activity_memory = build_activity_memory_context(
        activities,
    )

    return {
        **memory_context,
        "activity_memory": activity_memory,
    }


def build_activity_coach_prompt_context(
    activities: list[dict],
) -> dict:
    """
    Create clean context for AI prompts.
    """

    context = build_activity_memory_context(
        activities,
    )

    return {
        "recent_activity_count": (
            context["activity_context"]["activity_count"]
        ),
        "training_stress": (
            context["activity_context"]
            ["total_training_stress"]
        ),
        "fitness_trend": (
            context["activity_context"]
            ["fitness_trend"]
        ),
        "training_risk": (
            context["training_risk"]["risk"]
        ),
        "recommendation": (
            context["recommendation"]
            ["recommendation"]
        ),
    }
