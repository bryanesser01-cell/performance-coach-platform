from api.services.recovery_intelligence_service import (
    analyse_recovery_status,
    generate_recovery_recommendation,
)


def build_recovery_memory_context(
    recovery_data: dict,
) -> dict:
    """
    Build recovery intelligence context.

    Uses:
    - Readiness score
    - Recovery status
    - Recommendation
    """

    readiness_score = recovery_data.get(
        "readiness_score",
        0,
    )

    recovery_status = analyse_recovery_status(
        readiness_score,
    )

    recommendation = generate_recovery_recommendation(
        readiness_score,
    )

    return {
        "readiness_score": readiness_score,
        "recovery_status": recovery_status,
        "recommendation": recommendation,
    }


def enrich_coach_memory_with_recovery(
    memory_context: dict,
    recovery_data: dict,
) -> dict:
    """
    Add recovery intelligence into
    existing AI Coach memory.
    """

    recovery_context = build_recovery_memory_context(
        recovery_data,
    )

    return {
        **memory_context,
        "recovery_memory": recovery_context,
    }


def build_recovery_coach_prompt_context(
    recovery_data: dict,
) -> dict:
    """
    Create clean recovery context
    for AI Coach prompts.
    """

    context = build_recovery_memory_context(
        recovery_data,
    )

    return {
        "readiness_score": (context["readiness_score"]),
        "recovery_status": (context["recovery_status"]["status"]),
        "recovery_message": (context["recovery_status"]["message"]),
        "recommendation": (context["recommendation"]["recommendation"]),
    }


def generate_readiness_recommendation(
    recovery_data: dict,
) -> str:
    """
    Generate simple AI Coach recommendation.
    """

    context = build_recovery_coach_prompt_context(
        recovery_data,
    )

    return context["recommendation"]
