def evaluate_coaching_decision(
    readiness_score: int,
    fatigue_score: int,
    training_load: int,
) -> dict:
    """
    Evaluate athlete state and make
    a coaching decision.

    Decision rules:

    Low readiness or high fatigue
        -> RECOVERY

    High readiness
        -> TRAIN

    Otherwise
        -> MAINTAIN
    """

    if readiness_score < 60 or fatigue_score > 70:
        decision = "RECOVERY"

    elif readiness_score >= 80:
        decision = "TRAIN"

    else:
        decision = "MAINTAIN"

    return {
        "decision": decision,
        "readiness_score": readiness_score,
        "fatigue_score": fatigue_score,
        "training_load": training_load,
    }


def generate_coach_recommendation(
    decision: str,
) -> dict:
    """
    Generate recommendation from
    coaching decision.
    """

    recommendations = {
        "RECOVERY": ("Take a recovery day " "or complete an easy session."),
        "TRAIN": ("Complete planned training " "with normal intensity."),
        "MAINTAIN": ("Train conservatively " "and monitor response."),
    }

    return {
        "decision": decision,
        "recommendation": (
            recommendations.get(
                decision,
                "Monitor athlete state.",
            )
        ),
    }


def build_coach_strategy(
    decision: str,
    recommendation: str,
    confidence: int,
) -> dict:
    """
    Build final coaching strategy.
    """

    strategy_map = {
        "RECOVERY": "RECOVERY_FIRST",
        "TRAIN": "PERFORMANCE_FOCUS",
        "MAINTAIN": "BALANCED_APPROACH",
    }

    return {
        "decision": decision,
        "recommendation": recommendation,
        "strategy": (
            strategy_map.get(
                decision,
                "MONITOR",
            )
        ),
        "confidence": confidence,
    }
