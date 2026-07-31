from api.models.coach_context import CoachContext

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
        or training_load_status in (
            "high",
            "high_fatigue",
        )
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
    athlete_id: int | None = None,
    athlete_state: dict | None = None,
    memory_context: dict | None = None,
    context: CoachContext | None = None,
) -> dict:
    """
    Generate an adaptive coaching decision.

    Supports both the legacy API and CoachContext.
    """

    #
    # New CoachContext API
    #
    if context is not None:

        readiness = context.athlete_state.get(
            "readiness",
            {},
        )

        training = context.athlete_state.get(
            "training",
            {},
        )

        performance = context.athlete_state.get(
            "performance",
            {},
        )

        race = context.race_intelligence

        result = generate_coach_decision(
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
            days_to_race=race.get(
                "days_until_race",
            ),
            memory_context=context.memory_context,
        )

        confidence = calculate_decision_confidence(
            athlete_id=context.athlete_id,
            decision=result["decision"],
        )

        result = {
            **result,
            "athlete_id": context.athlete_id,
            "learning_confidence": confidence,
            "learning_context": {
                "decision": result["decision"],
                "confidence": confidence,
                "memory_count": len(
                    context.memory_context.get(
                        "memories",
                        [],
                    )
                ),
                "previous_decisions": len(
                    context.memory_context.get(
                        "decisions",
                        [],
                    )
                ),
            },
        }

        context.decision = result

        return result

    #
    # Legacy API
    #
    athlete_state = athlete_state or {}
    memory_context = memory_context or {}

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

    result = generate_coach_decision(
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
        decision=result["decision"],
    )

    return {
        **result,
        "athlete_id": athlete_id,
        "learning_confidence": confidence,
        "learning_context": {
            "decision": result["decision"],
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
