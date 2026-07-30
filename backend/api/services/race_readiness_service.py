"""
Race Readiness Service

Responsible for:
- calculating race readiness score
- analysing preparation status
- generating athlete race readiness insights
"""


def calculate_race_readiness_score(
    training_consistency: int,
    performance_trend: str,
    recovery_status: str,
    recent_training_load: str,
) -> dict:
    """
    Calculate race readiness score.

    Inputs:
    - training consistency
    - performance trend
    - recovery
    - training load

    Output:
    readiness score and status
    """

    score = 0


    # Training consistency
    if training_consistency >= 80:
        score += 30

    elif training_consistency >= 50:
        score += 20

    else:
        score += 10


    # Performance trend
    if performance_trend == "improving":
        score += 30

    elif performance_trend == "stable":
        score += 20


    # Recovery
    if recovery_status == "good":
        score += 25

    elif recovery_status == "moderate":
        score += 15


    # Training load
    if recent_training_load == "appropriate":
        score += 15

    elif recent_training_load == "high":
        score += 5


    if score >= 80:
        status = "ready"

    elif score >= 60:
        status = "developing"

    else:
        status = "not_ready"


    return {
        "readiness_score": score,

        "status": status,
    }



def analyse_race_readiness(
    athlete_data: dict,
) -> dict:
    """
    Analyse athlete race preparation.
    """

    readiness = calculate_race_readiness_score(
        training_consistency=athlete_data.get(
            "training_consistency",
            0,
        ),

        performance_trend=athlete_data.get(
            "performance_trend",
            "unknown",
        ),

        recovery_status=athlete_data.get(
            "recovery_status",
            "unknown",
        ),

        recent_training_load=athlete_data.get(
            "recent_training_load",
            "unknown",
        ),
    )


    return {
        "athlete": athlete_data,

        "race_readiness": readiness,
    }



def generate_race_readiness_summary(
    readiness_result: dict,
) -> dict:
    """
    Generate athlete-facing message.
    """

    status = readiness_result[
        "race_readiness"
    ][
        "status"
    ]


    return {
        "status": status,

        "message": (
            f"Race readiness status is "
            f"{status}. "
            "Assessment is based on "
            "recent training indicators."
        ),
    }

def generate_race_readiness_report(
    training_load: int,
    performance_score: int,
    fatigue_score: int,
    consistency_score: int,
) -> dict:
    """
    Generate race readiness report.

    Used by athlete performance reporting layer.

    Scores:
    - training load
    - performance
    - fatigue
    - consistency
    """

    readiness_score = round(
        (
            training_load
            +
            performance_score
            +
            fatigue_score
            +
            consistency_score
        )
        /
        4
    )


    if readiness_score >= 85:
        status = "ready"

    elif readiness_score >= 65:
        status = "developing"

    else:
        status = "not_ready"


    return {
    "race_readiness_score": readiness_score,

    "readiness_score": readiness_score,

    "status": status,

    "training_load": training_load,

    "performance_score": performance_score,

    "fatigue_score": fatigue_score,

    "consistency_score": consistency_score,

    "recommendation": (
        "Athlete is ready to race."
        if status == "ready"
        else
        "Continue preparation."
    ),
}
