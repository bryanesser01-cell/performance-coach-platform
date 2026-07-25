import logging
from datetime import date, timedelta
from statistics import fmean

from config.settings import settings
from database.training_models import TrainingSession
from schemas.analysis import PerformanceAnalysis

logger = logging.getLogger(__name__)


def _empty_analysis() -> PerformanceAnalysis:
    """
    Return an empty performance analysis.
    """
    return PerformanceAnalysis(
        total_sessions=0,
        total_distance=0.0,
        total_duration=0.0,
        average_pace=0.0,
        average_heart_rate=0.0,
        average_rpe=0.0,
        total_training_load=0.0,
        longest_run=0.0,
        coach_comment="No training data is available yet.",
        strengths=[],
        risks=["No training sessions recorded."],
        recommendations=["Record training sessions to begin performance analysis."],
    )


def analyse_training(
    sessions: list[TrainingSession],
) -> PerformanceAnalysis:
    """
    Analyse recent training sessions and return performance metrics
    together with coaching insights.

    Weekly metrics are calculated using only sessions completed
    within the configured analysis window.
    """

    logger.info(
        "Analysing %s training sessions.",
        len(sessions),
    )

    if not sessions:
        logger.info("No training sessions available.")
        return _empty_analysis()

    analysis_window = date.today() - timedelta(days=settings.ANALYSIS_WINDOW_DAYS)

    weekly_sessions = [
        session for session in sessions if session.date >= analysis_window
    ]

    if not weekly_sessions:
        logger.info(
            "No sessions found within the analysis window. "
            "Using all available sessions."
        )
        weekly_sessions = sessions

    total_sessions = len(weekly_sessions)

    total_distance = sum(session.distance for session in weekly_sessions)

    total_duration = sum(session.duration for session in weekly_sessions)

    average_pace = total_duration / total_distance if total_distance > 0 else 0.0

    heart_rates = [
        session.average_hr
        for session in weekly_sessions
        if session.average_hr is not None
    ]

    average_heart_rate = fmean(heart_rates) if heart_rates else 0.0

    rpe_values = [session.rpe for session in weekly_sessions if session.rpe is not None]

    average_rpe = fmean(rpe_values) if rpe_values else 0.0

    total_training_load = sum(
        session.training_load or 0.0 for session in weekly_sessions
    )

    longest_run = max(
        (session.distance for session in weekly_sessions),
        default=0.0,
    )

    strengths: list[str] = []
    risks: list[str] = []
    recommendations: list[str] = []

    if average_rpe <= settings.TARGET_RPE:
        strengths.append("Training intensity is well balanced.")
    else:
        risks.append("Training intensity appears too high.")
        recommendations.append("Schedule an easier recovery session.")

    if total_sessions < settings.MIN_WEEKLY_SESSIONS:
        risks.append("Weekly training frequency is below the recommended target.")
        recommendations.append(
            f"Aim for at least {settings.MIN_WEEKLY_SESSIONS} running sessions each week."
        )
    else:
        strengths.append("Weekly training consistency is good.")

    if total_distance < settings.MIN_WEEKLY_DISTANCE:
        risks.append("Weekly running volume is below the recommended target.")
        recommendations.append("Increase weekly distance gradually by 5–10%.")
    else:
        strengths.append("Weekly running volume is appropriate.")

    if not recommendations:
        recommendations.extend(
            [
                "Maintain your current training consistency.",
                "Continue progressive overload while allowing adequate recovery.",
            ]
        )

    coach_comment = (
        "Training is progressing well."
        if not risks
        else (
            "Several factors should be addressed before increasing training intensity."
        )
    )

    logger.info(
        "Performance analysis completed successfully for %s sessions.",
        total_sessions,
    )

    return PerformanceAnalysis(
        total_sessions=total_sessions,
        total_distance=round(total_distance, 2),
        total_duration=round(total_duration, 2),
        average_pace=round(average_pace, 2),
        average_heart_rate=round(average_heart_rate, 1),
        average_rpe=round(average_rpe, 1),
        total_training_load=round(total_training_load, 1),
        longest_run=round(longest_run, 2),
        coach_comment=coach_comment,
        strengths=strengths,
        risks=risks,
        recommendations=recommendations,
    )
