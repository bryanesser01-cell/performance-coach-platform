import logging

from schemas.analysis import PerformanceAnalysis
from schemas.recommendation import Recommendation

logger = logging.getLogger(__name__)


def generate_recommendations(
    analysis: PerformanceAnalysis,
) -> list[Recommendation]:
    """
    Generate prioritised coaching recommendations based on
    the athlete's performance analysis.
    """

    logger.info("Generating coaching recommendations.")

    recommendations: list[Recommendation] = []

    if analysis.total_sessions < 3:
        recommendations.append(
            Recommendation(
                priority=1,
                category="Consistency",
                title="Increase Training Frequency",
                description="Aim for at least three running sessions each week.",
            )
        )

    if analysis.total_distance < 25:
        recommendations.append(
            Recommendation(
                priority=2,
                category="Volume",
                title="Build Weekly Distance",
                description="Increase weekly running volume by approximately 10%.",
            )
        )

    if analysis.total_training_load > 500:
        recommendations.append(
            Recommendation(
                priority=1,
                category="Recovery",
                title="Reduce Fatigue",
                description="Schedule an easy recovery run or complete rest day.",
            )
        )

    if analysis.average_rpe >= 8:
        recommendations.append(
            Recommendation(
                priority=2,
                category="Intensity",
                title="Reduce Training Intensity",
                description="Several recent sessions have been very hard.",
            )
        )

    recommendations = sorted(
        recommendations,
        key=lambda r: r.priority,
    )

    logger.info(
        "Generated %s recommendations.",
        len(recommendations),
    )

    return recommendations