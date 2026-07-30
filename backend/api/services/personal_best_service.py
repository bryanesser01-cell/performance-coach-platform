"""
Personal Best Service

Responsible for:
- storing athlete personal bests
- comparing performances
- calculating improvement
- generating PB summaries
"""


def record_personal_best(
    event: str,
    time_seconds: float,
    date: str,
) -> dict:
    """
    Create personal best record.
    """

    return {
        "event": event,

        "time_seconds": time_seconds,

        "date": date,
    }



def calculate_improvement(
    previous_time_seconds: float,
    current_time_seconds: float,
) -> dict:
    """
    Calculate performance improvement.

    Lower time is better for running events.
    """

    difference = (
        previous_time_seconds
        -
        current_time_seconds
    )


    if previous_time_seconds == 0:

        percentage = 0

    else:

        percentage = (
            difference
            /
            previous_time_seconds
        ) * 100


    if difference > 0:

        trend = "improving"


    elif difference < 0:

        trend = "declining"


    else:

        trend = "stable"


    return {
        "improvement_seconds": round(
            difference,
            2,
        ),

        "improvement_percentage": round(
            percentage,
            2,
        ),

        "trend": trend,
    }



def compare_personal_best(
    previous_pb: dict,
    current_pb: dict,
) -> dict:
    """
    Compare previous and current PB.
    """

    improvement = calculate_improvement(
        previous_pb["time_seconds"],
        current_pb["time_seconds"],
    )


    return {
        "event": current_pb["event"],

        "previous": previous_pb,

        "current": current_pb,

        "improvement": improvement,
    }



def generate_personal_best_summary(
    comparison: dict,
) -> dict:
    """
    Generate athlete-facing PB summary.
    """

    improvement = comparison[
        "improvement"
    ]


    return {
        "message": (
            f"Your {comparison['event']} "
            "performance is "
            f"{improvement['trend']}."
        ),

        "improvement_seconds": (
            improvement[
                "improvement_seconds"
            ]
        ),

        "improvement_percentage": (
            improvement[
                "improvement_percentage"
            ]
        ),
    }
