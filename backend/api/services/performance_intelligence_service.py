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

    total_distance = 0.0
    total_minutes = 0.0

    for session in sessions:
        total_distance += session.get(
            "distance_km",
            0.0,
        )

        total_minutes += session.get(
            "duration_minutes",
            0.0,
        )

    if total_distance == 0:
        return "0:00/km"

    pace = total_minutes / total_distance

    minutes = int(pace)
    seconds = int(round((pace - minutes) * 60))

    return f"{minutes}:{seconds:02d}/km"


def analyse_performance_trend(
    sessions: list[dict],
) -> dict:
    """
    Analyse whether performance is improving or declining.
    """

    if len(sessions) < 2:
        return {
            "trend": "insufficient_data",
            "confidence": "low",
        }

    first_pace = sessions[0].get(
        "pace_seconds",
        0,
    )

    last_pace = sessions[-1].get(
        "pace_seconds",
        0,
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
        "sessions_analysed": len(sessions),
    }


def calculate_training_consistency(
    sessions: list[dict],
) -> dict:
    """
    Measure training consistency.
    """

    completed = len(sessions)

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


def analyse_performance_intelligence(
    sessions: list[dict],
) -> dict:
    """
    Generate structured performance intelligence
    for the AI Coach.

    Combines trend analysis, consistency,
    average pace and improvement metrics
    into a single intelligence payload.
    """

    trend = analyse_performance_trend(
        sessions,
    )

    consistency = calculate_training_consistency(
        sessions,
    )

    average_pace = calculate_average_pace(
        sessions,
    )

    #
    # Not enough data
    #
    if len(sessions) < 6:
        return {
            "trend": trend.get(
                "trend",
                "insufficient_data",
            ),
            "confidence": 0.30,
            "average_pace": average_pace,
            "improvement_rate": 0.0,
            "plateau": False,
            "declining": False,
            "consistency_score": consistency.get(
                "consistency_score",
                0,
            ),
            "fatigue_adjusted": False,
            "recommendation": "collect_more_data",
        }

    midpoint = len(sessions) // 2

    first_half = sessions[:midpoint]
    second_half = sessions[midpoint:]

    previous_average = (
        sum(
            session.get(
                "pace_seconds",
                0,
            )
            for session in first_half
        )
        / len(first_half)
    )

    recent_average = (
        sum(
            session.get(
                "pace_seconds",
                0,
            )
            for session in second_half
        )
        / len(second_half)
    )

    improvement_rate = (
        previous_average - recent_average
    ) / previous_average

    plateau = (
        abs(previous_average - recent_average)
        < 3
    )

    declining = (
        recent_average > previous_average
    )

    if plateau:
        recommendation = "maintain"

    elif declining:
        recommendation = "investigate"

    elif improvement_rate > 0.02:
        recommendation = "progress"

    else:
        recommendation = "maintain"

    confidence = min(
        1.0,
        0.50
        + (
            consistency.get(
                "consistency_score",
                0,
            )
            / 200
        ),
    )

    return {
        "trend": trend.get(
            "trend",
            "stable",
        ),
        "confidence": round(
            confidence,
            2,
        ),
        "average_pace": average_pace,
        "improvement_rate": round(
            improvement_rate,
            3,
        ),
        "plateau": plateau,
        "declining": declining,
        "consistency_score": consistency.get(
            "consistency_score",
            0,
        ),
        "fatigue_adjusted": False,
        "recommendation": recommendation,
    }
