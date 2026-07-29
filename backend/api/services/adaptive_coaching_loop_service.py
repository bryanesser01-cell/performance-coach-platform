from api.services.adaptive_coach_decision_service import (
    generate_coach_decision,
)
from api.services.workout_completion_analysis_service import (
    analyse_workout_completion,
)


def run_adaptive_coaching_loop(
    planned_workout: dict,
    athlete_feedback: dict,
    readiness_score: int,
    training_load_status: str,
    performance_trend: str,
    days_to_race: int | None = None,
) -> dict:
    """
    Complete adaptive coaching loop.

    Flow:
    1. Analyse completed workout
    2. Generate adaptive coaching decision
    3. Return combined coach recommendation
    """

    workout_analysis = (
        analyse_workout_completion(
            planned_workout=planned_workout,
            athlete_feedback=athlete_feedback,
        )
    )

    coach_decision = (
        generate_coach_decision(
            readiness_score=readiness_score,
            training_load_status=training_load_status,
            performance_trend=performance_trend,
            days_to_race=days_to_race,
        )
    )

    return {
        "workout_analysis": workout_analysis,
        "coach_decision": coach_decision,
        "next_action": coach_decision.get(
            "decision",
        ),
        "recommendation": coach_decision.get(
            "recommendation",
        ),
        "reason": coach_decision.get(
            "reason",
        ),
    }
