import logging
from statistics import mean

from config.settings import settings
from schemas.analysis import PerformanceAnalysis
from schemas.training import TrainingSessionResponse

logger = logging.getLogger(__name__)


def analyse_training(
    sessions: list[TrainingSessionResponse],
) -> PerformanceAnalysis | None:
    """
    Analyse a collection of training sessions and return
    a PerformanceAnalysis object containing metrics and
    coaching insights.
    """

    if not sessions:
        return None

    logger.info(
        "Analysing %s training sessions.",
        len(sessions),
    )

    # -----------------------------
    # Performance Metrics
    # -----------------------------

    total_sessions = len(sessions)

    total_distance = sum(
        s.distance for s in sessions
    )

    total_duration = sum(
        s.duration for s in sessions
    )

    average_pace = mean(
        s.average_pace
        for s in sessions
    )

    hr_values = [
        s.average_hr
        for s in sessions
        if s.average_hr is not None
    ]

    average_hr = (
        mean(hr_values)
        if hr_values
        else 0
    )

    rpe_values = [
        s.rpe
        for s in sessions
        if s.rpe is not None
    ]

    average_rpe = (
        mean(rpe_values)
        if rpe_values
        else 0
    )

    total_training_load = sum(
        s.training_load or 0
        for s in sessions
    )

    longest_run = max(
        s.distance
        for s in sessions
    )

    # -----------------------------
    # Coach Reasoning
    # -----------------------------

    strengths = []
    risks = []
    recommendations = []

    # Intensity
    if average_rpe <= settings.TARGET_RPE:
        strengths.append(
            "Training intensity is well balanced."
        )
    else:
        risks.append(
            "Training intensity may be too high."
        )
        recommendations.append(
            "Schedule an easier recovery session."
        )

    # Frequency
    if total_sessions < settings.MIN_WEEKLY_SESSIONS:
        risks.append(
            "Training frequency is low."
        )
        recommendations.append(
            (
                f"Aim for at least "
                f"{settings.MIN_WEEKLY_SESSIONS} "
                f"running sessions per week."
            )
        )
    else:
        strengths.append(
            "Training consistency is improving."
        )

    # Weekly Volume
    if total_distance < settings.MIN_WEEKLY_DISTANCE:
        risks.append(
            "Weekly running volume is below target."
        )
        recommendations.append(
            "Gradually increase weekly distance by 5–10%."
        )
    else:
        strengths.append(
            "Weekly running volume is solid."
        )

    # -----------------------------
    # Overall Coach Comment
    # -----------------------------

    if risks:
        coach_comment = (
            "Several factors need attention before increasing training intensity."
        )
    else:
        coach_comment = (
            "Training is progressing well. Continue building consistently."
        )

    # -----------------------------
    # Return Analysis
    # -----------------------------

    logger.info(
        "Performance analysis completed successfully."
    )

    return PerformanceAnalysis(
        total_sessions=total_sessions,
        total_distance=round(total_distance, 2),
        total_duration=round(total_duration, 2),
        average_pace=round(average_pace, 2),
        average_heart_rate=round(average_hr, 1),
        average_rpe=round(average_rpe, 1),
        total_training_load=round(total_training_load, 1),
        longest_run=round(longest_run, 2),
        coach_comment=coach_comment,
        strengths=strengths,
        risks=risks,
        recommendations=recommendations,
    )
