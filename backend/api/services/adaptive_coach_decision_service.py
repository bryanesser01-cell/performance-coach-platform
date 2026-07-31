from api.services.coach_learning_memory_service import (
    calculate_decision_confidence,
)


def generate_coach_decision(
    readiness_score: int,
    training_load_status: str,
    performance_trend: str,
    days_to_race: int | None = None,
    memory_context: dict | None = None,
) -> dict:
    """
    Generate adaptive coaching decision.
    """

    if memory_context is None:
        memory_context = {}

    memories = memory_context.get("memories", [])
    previous_decisions = memory_context.get("decisions", [])

    if (
        days_to_race is not None
        and days_to_race <= 14
        and readiness_score >= 80
    ):
        return {
            "decision": "RACE_TAPER",
            "recommendation": (
                "Reduce training volume and "
                "prioritise freshness."
            ),
            "reason": (
                "Race is approaching with "
                "high readiness."
            ),
        }

    if (
        readiness_score < 60
        or training_load_status == "high_fatigue"
        or training_load_status == "high"
    ):
        return {
            "decision": "REDUCE_TRAINING",
            "recommendation": (
                "Reduce intensity and focus "
                "on recovery."
            ),
            "reason": (
                "Recovery indicators require "
                "attention."
            ),
        }

    if (
        performance_trend == "improving"
        and readiness_score >= 75
    ):
        return {
            "decision": "PROGRESS_TRAINING",
            "recommendation": (
                "Progress training carefully "
                "while maintaining recovery."
            ),
            "reason": (
                "Performance and readiness "
                "are improving."
            ),
        }

    if (
        readiness_score >= 70
        and training_load_status == "stable"
    ):
        return {
            "decision": "MAINTAIN_TRAINING",
            "recommendation": (
                "Continue the current training plan."
            ),
            "reason": (
                "Training load and recovery "
                "are balanced."
            ),
        }

    return {
        "decision": "RECOVERY_SESSION",
        "recommendation": (
            "Complete an easy recovery session."
        ),
        "reason": (
            "Current indicators suggest caution."
        ),
    }


def generate_adaptive_coach_decision(
    athlete_id: int,
    athlete_state: dict,
    memory_context: dict | None = None,
) -> dict:
    """
    Generate a decision using athlete state,
    previous learning history and memory context.

    Flow:

        Athlete State
              ↓
        Memory Context
              ↓
        Decision Engine
              ↓
        Learning Memory
              ↓
        Confidence Score
    """

    if memory_context is None:
        memory_context = {}

    readiness = athlete_state.get(
        "readiness",
        {},
    )

    training = athlete_state.get(
        "training",
        {},
    )

    performance = athlete_state.get(
        "performance",
        {},
    )

    decision = generate_coach_decision(
        readiness_score=readiness.get(
            "score",
            0,
        ),
        training_load_status=training.get(
            "load_status",
            "unknown",
        ),
        performance_trend=performance.get(
            "trend",
            "unknown",
        ),
        memory_context=memory_context,
    )

    confidence = calculate_decision_confidence(
        athlete_id=athlete_id,
        decision=decision["decision"],
    )

    return {
        **decision,
        "athlete_id": athlete_id,
        "learning_confidence": confidence,
        "learning_context": {
            "decision": decision["decision"],
            "confidence": confidence,
            "memory_count": len(
                memory_context.get(
                    "memories",
                    [],
                )
            ),
            "previous_decisions": len(
                memory_context.get(
                    "decisions",
                    [],
                )
            ),
        },
    }
