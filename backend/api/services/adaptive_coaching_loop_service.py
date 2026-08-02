from api.services.adaptive_coach_decision_service import (
    generate_adaptive_coach_decision,
    generate_coach_decision,
)
from api.services.adaptive_learning_loop_service import (
    record_adaptive_coaching_decision,
)
from api.services.athlete_state_service import (
    get_athlete_state,
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
    2. Generate coaching decision
    3. Return recommendation
    """

    workout_analysis = analyse_workout_completion(
        planned_workout=planned_workout,
        athlete_feedback=athlete_feedback,
    )

    coach_decision = generate_coach_decision(
        readiness_score=readiness_score,
        training_load_status=training_load_status,
        performance_trend=performance_trend,
        days_to_race=days_to_race,
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


def run_adaptive_coaching_cycle(
    db,
    athlete_id: int,
    planned_workout: dict,
    athlete_feedback: dict,
) -> dict:
    """
    Complete adaptive coaching cycle.

    Flow:

    Athlete State
          ↓
    Workout Analysis
          ↓
    Adaptive Decision Engine
          ↓
    Coaching Recommendation
    """

    athlete_state = get_athlete_state(
        db,
        athlete_id,
    )

    workout_analysis = analyse_workout_completion(
        planned_workout=planned_workout,
        athlete_feedback=athlete_feedback,
    )

    decision = generate_adaptive_coach_decision(
        athlete_id,
        athlete_state,
    )

    decision_record = record_adaptive_coaching_decision(
        db=db,
        athlete_id=athlete_id,
        decision=decision,
    )

    return {
        "athlete_id": athlete_id,
        "athlete_state": athlete_state,
        "workout_analysis": workout_analysis,
        "decision": decision,
        "decision_record": decision_record,
        "next_action": decision.get(
            "decision",
        ),
        "recommendation": decision.get(
            "recommendation",
        ),
        "reason": decision.get(
            "reason",
        ),
        "adaptive": True,
    }
