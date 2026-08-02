def calculate_training_load(
    sessions: list[dict],
) -> dict:
    """
    Calculate recent training load.

    Uses:
    - duration
    - intensity
    - session history
    """

    total_load = 0

    for session in sessions:

        duration = session.get(
            "duration_minutes",
            0,
        )

        intensity = session.get(
            "intensity",
            1,
        )

        total_load += duration * intensity

    return {
        "training_load": total_load,
        "sessions_completed": len(sessions),
    }


def calculate_weekly_load_change(
    current_load: float,
    previous_load: float,
) -> dict:
    """
    Calculate training load increase.

    Used to identify sudden spikes.
    """

    if previous_load == 0:

        change = 0

    else:

        change = ((current_load - previous_load) / previous_load) * 100

    return {
        "current_load": current_load,
        "previous_load": previous_load,
        "change_percent": round(
            change,
            2,
        ),
    }


def classify_fatigue_level(
    fatigue_score: int,
) -> str:
    """
    Classify athlete fatigue.
    """

    if fatigue_score >= 80:

        return "HIGH"

    if fatigue_score >= 50:

        return "MODERATE"

    return "LOW"


def calculate_recovery_status(
    sleep_hours: float,
    fatigue_score: int,
    resting_hr_change: int,
) -> dict:
    """
    Determine recovery readiness.
    """

    issues = []

    if sleep_hours < 7:

        issues.append("insufficient_sleep")

    if fatigue_score >= 70:

        issues.append("high_fatigue")

    if resting_hr_change >= 10:

        issues.append("elevated_resting_heart_rate")

    if len(issues) >= 2:

        readiness = "REDUCE_TRAINING"

    elif len(issues) == 1:

        readiness = "MODIFY_SESSION"

    else:

        readiness = "READY"

    return {
        "readiness": readiness,
        "issues": issues,
    }


def recommend_training_adjustment(
    recovery_status: str,
    planned_session: str,
) -> dict:
    """
    Adjust training recommendation
    based on recovery.
    """

    if recovery_status == "READY":

        recommendation = planned_session

        reason = "Athlete readiness supports " "planned training."

    elif recovery_status == "MODIFY_SESSION":

        recommendation = "Reduce intensity and volume"

        reason = "Minor recovery concerns detected."

    else:

        recommendation = "Recovery session or rest"

        reason = "Recovery markers suggest " "additional adaptation time."

    return {
        "original_session": planned_session,
        "recommended_session": recommendation,
        "reason": reason,
    }


def build_training_readiness_report(
    sessions: list[dict],
    sleep_hours: float,
    fatigue_score: int,
    resting_hr_change: int,
) -> dict:
    """
    Build complete readiness report.
    """

    load = calculate_training_load(
        sessions,
    )

    recovery = calculate_recovery_status(
        sleep_hours=sleep_hours,
        fatigue_score=fatigue_score,
        resting_hr_change=resting_hr_change,
    )

    return {
        "training_load": load,
        "fatigue_level": (classify_fatigue_level(fatigue_score)),
        "recovery": recovery,
        "ready_to_train": (recovery["readiness"] == "READY"),
    }
