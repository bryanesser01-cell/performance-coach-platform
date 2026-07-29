from api.services.adaptive_coach_decision_service import (
    generate_coach_decision,
)


def build_coach_context(
    athlete_id: int,
    goal: str,
    readiness_score: int,
    training_load_status: str,
    performance_trend: str,
    memories: list[str] | None = None,
    days_to_race: int | None = None,
) -> dict:
    """
    Build complete athlete context for AI coach.

    Combines:
    - Athlete goal
    - Readiness
    - Training load
    - Performance trend
    - Memory
    - Race timeline
    - Coaching decision
    """

    decision = generate_coach_decision(
        readiness_score=readiness_score,
        training_load_status=training_load_status,
        performance_trend=performance_trend,
        days_to_race=days_to_race,
    )

    return {
        "athlete_id": athlete_id,
        "goal": goal,
        "readiness_score": readiness_score,
        "training_load_status": training_load_status,
        "performance_trend": performance_trend,
        "memories": memories or [],
        "decision": decision,
    }


def generate_coach_summary(
    context: dict,
) -> str:
    """
    Generate human readable coach context summary.
    """

    decision = context["decision"]

    return (
        f"Athlete goal: {context['goal']}. "
        f"Readiness score: {context['readiness_score']}. "
        f"Current recommendation: "
        f"{decision['recommendation']}"
    )
