"""
Performance Intelligence Service

Responsible for:
- analysing athlete performance trends
- detecting improvement
- measuring consistency
- generating performance insights
"""


def calculate_average_pace(
    sessions: list[dict],
) -> str:
    """
    Calculate average pace from sessions.
    """

    if not sessions:
        return "0:00/km"


    total_distance = 0

    total_minutes = 0


    for session in sessions:

        total_distance += session.get(
            "distance_km",
            0,
        )

        total_minutes += session.get(
            "duration_minutes",
            0,
        )


    if total_distance == 0:

        return "0:00/km"


    pace = (
        total_minutes
        /
        total_distance
    )


    minutes = int(pace)

    seconds = int(
        round(
            (pace - minutes)
            * 60
        )
    )


    return (
        f"{minutes}:{seconds:02d}/km"
    )



def analyse_performance_trend(
    sessions: list[dict],
) -> dict:
    """
    Analyse whether performance
    is improving or declining.
    """

    if len(sessions) < 2:

        return {
            "trend": "insufficient_data",

            "confidence": "low",
        }


    first_session = sessions[0]

    last_session = sessions[-1]


    first_pace = (
        first_session.get(
            "pace_seconds",
            0,
        )
    )


    last_pace = (
        last_session.get(
            "pace_seconds",
            0,
        )
    )


    if last_pace < first_pace:

        trend = "improving"


    elif last_pace > first_pace:

        trend = "declining"


    else:

        trend = "stable"


    return {
        "trend": trend,

        "confidence": "medium",

        "sessions analysed": len(
            sessions
        ),
    }



def calculate_training_consistency(
    sessions: list[dict],
) -> dict:
    """
    Measure training consistency.
    """

    completed = len(
        sessions
    )


    if completed == 0:

        score = 0


    elif completed >= 4:

        score = 100


    else:

        score = completed * 25


    return {
        "consistency_score": score,

        "sessions_completed": completed,
    }



def generate_performance_insight(
    sessions: list[dict],
) -> dict:
    """
    Generate athlete-facing insight.
    """

    trend = analyse_performance_trend(
        sessions,
    )


    consistency = calculate_training_consistency(
        sessions,
    )


    return {
        "performance_trend": trend,

        "training_consistency": consistency,

        "insight": (
            "Performance analysis completed "
            "using recent training history."
        ),
    }
