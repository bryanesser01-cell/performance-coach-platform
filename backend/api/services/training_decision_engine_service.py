def evaluate_training_readiness(
    readiness_score: int,
    fatigue_score: int,
    performance_trend: str,
) -> dict:
    """
    Evaluate athlete readiness for training.

    Determines whether athlete is:
    - READY
    - CAUTION
    - RECOVERY_REQUIRED
    """

    if (
        readiness_score >= 80
        and fatigue_score < 40
    ):
        status = "READY"

    elif fatigue_score >= 70:
        status = "RECOVERY_REQUIRED"

    else:
        status = "CAUTION"

    return {
        "readiness_status": status,
        "readiness_score": readiness_score,
        "fatigue_score": fatigue_score,
        "performance_trend": performance_trend,
    }


def select_training_intensity(
    readiness_status: str,
    performance_trend: str,
) -> dict:
    """
    Select training intensity based
    on athlete state.
    """

    if readiness_status == "READY":
        intensity = "HIGH"

    elif readiness_status == "CAUTION":
        intensity = "MODERATE"

    else:
        intensity = "LOW"

    return {
        "intensity": intensity,
        "performance_trend": performance_trend,
    }


def generate_daily_training_decision(
    readiness_score: int,
    fatigue_score: int,
    performance_trend: str,
) -> dict:
    """
    Generate complete daily training decision.

    Flow:

    Athlete Intelligence
          ↓
    Readiness Evaluation
          ↓
    Intensity Selection
          ↓
    Daily Decision
    """

    readiness = evaluate_training_readiness(
        readiness_score=readiness_score,
        fatigue_score=fatigue_score,
        performance_trend=performance_trend,
    )

    intensity = select_training_intensity(
        readiness_status=readiness[
            "readiness_status"
        ],
        performance_trend=performance_trend,
    )

    if (
        readiness["readiness_status"]
        == "RECOVERY_REQUIRED"
    ):
        decision = "RECOVER"

    elif intensity["intensity"] == "HIGH":
        decision = "TRAIN_HARD"

    elif intensity["intensity"] == "MODERATE":
        decision = "TRAIN_MODERATE"

    else:
        decision = "EASY_SESSION"

    return {
        "decision": decision,
        "readiness": readiness,
        "training_intensity": intensity[
            "intensity"
        ],
    }
