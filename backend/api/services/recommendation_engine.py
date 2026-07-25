import logging

from config.settings import settings
from schemas.analysis import PerformanceAnalysis
from schemas.recommendation import Recommendation

logger = logging.getLogger(__name__)


def generate_recommendations(
    analysis: PerformanceAnalysis,
) -> list[Recommendation]:
    """
    Generate prioritised coaching recommendations based on
    an athlete's performance analysis.
    """

    logger.info("Generating coaching recommendations.")

    recommendations: list[Recommendation] = []

    # -------------------------------------------------
    # Training Frequency
    # -------------------------------------------------

    if analysis.total_sessions < settings.min_weekly_sessions:
        recommendations.append(
            Recommendation(
                priority=1,
                category="Consistency",
                title="Increase Training Frequency",
                description=(
                    f"Aim for at least "
                    f"{settings.min_weekly_sessions} "
                    "running sessions each week."
                ),
            )
        )

    # -------------------------------------------------
    # Weekly Volume
    # -------------------------------------------------

    if analysis.total_distance < settings.min_weekly_distance:
        recommendations.append(
            Recommendation(
                priority=2,
                category="Volume",
                title="Build Weekly Distance",
                description=(
                    f"Increase weekly running volume gradually "
                    f"by up to {int(settings.max_weekly_distance_increase * 100)}%."
                ),
            )
        )

    # -------------------------------------------------
    # Recovery
    # -------------------------------------------------

    if analysis.total_training_load > settings.max_recommended_training_load:
        recommendations.append(
            Recommendation(
                priority=1,
                category="Recovery",
                title="Reduce Fatigue",
                description=(
                    "Schedule an easy recovery run or take a complete rest day."
                ),
            )
        )

    # -------------------------------------------------
    # Training Intensity
    # -------------------------------------------------

    if analysis.average_rpe > settings.target_rpe:
        recommendations.append(
            Recommendation(
                priority=2,
                category="Intensity",
                title="Reduce Training Intensity",
                description=(
                    "Several recent sessions have been harder than the target effort."
                ),
            )
        )

    # -------------------------------------------------
    # Positive Recommendation
    # -------------------------------------------------

    if not recommendations:
        recommendations.append(
            Recommendation(
                priority=3,
                category="Maintenance",
                title="Maintain Current Training",
                description=(
                    "Your recent training is well balanced. "
                    "Continue progressing gradually while "
                    "prioritising recovery."
                ),
            )
        )

    recommendations.sort(
        key=lambda recommendation: (
            recommendation.priority,
            recommendation.category,
        )
    )

    logger.info(
        "Generated %s coaching recommendations.",
        len(recommendations),
    )

    return recommendations
