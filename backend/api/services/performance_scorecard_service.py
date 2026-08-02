"""
Performance Scorecard Service

Creates an athlete performance snapshot.

Combines:
- fitness
- consistency
- readiness
- improvement trends
"""


def calculate_overall_score(
    fitness_score: int,
    consistency_score: int,
    readiness_score: int,
    improvement_score: int,
) -> int:
    """
    Calculate overall athlete score.
    """

    return round(
        (fitness_score + consistency_score + readiness_score + improvement_score) / 4
    )


def generate_performance_scorecard(
    fitness_score: int,
    consistency_score: int,
    readiness_score: int,
    improvement_score: int,
    trend: str,
) -> dict:
    """
    Generate athlete dashboard scorecard.
    """

    overall_score = calculate_overall_score(
        fitness_score,
        consistency_score,
        readiness_score,
        improvement_score,
    )

    if overall_score >= 85:
        status = "excellent"

    elif overall_score >= 70:
        status = "developing"

    else:
        status = "building"

    return {
        "overall_score": overall_score,
        "status": status,
        "fitness_score": fitness_score,
        "consistency_score": consistency_score,
        "readiness_score": readiness_score,
        "improvement_score": improvement_score,
        "trend": trend,
    }


def generate_scorecard_summary(
    scorecard: dict,
) -> dict:
    """
    Create athlete-facing dashboard message.
    """

    return {
        "headline": (f"Athlete status: " f"{scorecard['status']}"),
        "message": (
            f"Current performance score is "
            f"{scorecard['overall_score']}/100 "
            f"with a "
            f"{scorecard['trend']} trend."
        ),
    }
