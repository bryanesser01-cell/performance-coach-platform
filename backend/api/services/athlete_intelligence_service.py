def calculate_readiness_score(
    sleep_score: int,
    recovery_score: int,
    recent_training_load: int,
) -> dict:
    """
    Calculate athlete readiness score.

    Higher sleep and recovery improve readiness.
    High training load reduces readiness.

    Returns score 0-100.
    """

    score = (
        (sleep_score * 0.35)
        + (recovery_score * 0.45)
        - min(
            recent_training_load / 20,
            20,
        )
    )

    readiness = max(
        0,
        min(
            int(score),
            100,
        ),
    )

    return {
        "readiness_score": readiness,
        "sleep_score": sleep_score,
        "recovery_score": recovery_score,
        "training_load": recent_training_load,
    }


def calculate_training_fatigue(
    training_load: int,
    recovery_score: int,
) -> dict:
    """
    Calculate athlete fatigue score.

    Higher load increases fatigue.
    Better recovery reduces fatigue.

    Returns fatigue 0-100.
    """

    fatigue = (
        (training_load / 10)
        - (recovery_score * 0.4)
    )

    fatigue_score = max(
        0,
        min(
            int(fatigue),
            100,
        ),
    )

    return {
        "fatigue_score": fatigue_score,
        "training_load": training_load,
        "recovery_score": recovery_score,
    }


def calculate_performance_trend(
    recent_performance: list[int],
) -> dict:
    """
    Analyse recent performance trend.

    Positive improvement:
        IMPROVING

    Negative:
        DECLINING

    Stable:
        MAINTAINING
    """

    if len(recent_performance) < 2:
        trend = "INSUFFICIENT_DATA"

    else:
        first = recent_performance[0]
        last = recent_performance[-1]

        if last > first:
            trend = "IMPROVING"

        elif last < first:
            trend = "DECLINING"

        else:
            trend = "MAINTAINING"

    return {
        "trend": trend,
        "performance_history": recent_performance,
    }


def build_athlete_intelligence_profile(
    readiness_score: int,
    fatigue_score: int,
    performance_trend: str,
) -> dict:
    """
    Build athlete intelligence profile.
    """

    if readiness_score >= 80 and fatigue_score < 40:
        status = "READY_TO_PERFORM"

    elif fatigue_score > 70:
        status = "NEEDS_RECOVERY"

    else:
        status = "BALANCED"

    return {
        "status": status,
        "readiness_score": readiness_score,
        "fatigue_score": fatigue_score,
        "performance_trend": performance_trend,
    }
