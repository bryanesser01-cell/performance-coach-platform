from schemas.analysis import PerformanceAnalysis


def generate_coach_reasoning(
    analysis: PerformanceAnalysis,
):
    """
    Generates coaching insights based on performance analysis.
    """

    comments = []
    strengths = []
    risks = []
    recommendations = []

    # ------------------------
    # Training Frequency
    # ------------------------

    if analysis.total_sessions < 3:
        risks.append("Training frequency is low.")
        recommendations.append(
            "Aim for at least 3 running sessions per week."
        )
    else:
        strengths.append("Good training consistency.")

    # ------------------------
    # Weekly Distance
    # ------------------------

    if analysis.total_distance < 25:
        risks.append("Weekly running volume is below target.")
        recommendations.append(
            "Gradually increase weekly distance by 5–10%."
        )
    else:
        strengths.append("Solid weekly running volume.")

    # ------------------------
    # Training Intensity
    # ------------------------

    if analysis.average_rpe >= 8:
        risks.append("Recent training intensity is very high.")
        recommendations.append(
            "Schedule an easy recovery run."
        )
    else:
        strengths.append("Training intensity is well balanced.")

    # ------------------------
    # Training Load
    # ------------------------

    if analysis.total_training_load > 500:
        risks.append("High accumulated training load.")
        recommendations.append(
            "Monitor fatigue and prioritise recovery."
        )

    # ------------------------
    # Overall Coach Comment
    # ------------------------

    if len(risks) == 0:
        comments.append(
            "Excellent training week. Maintain your current progression."
        )

    elif len(risks) == 1:
        comments.append(
            "Training is progressing well with one area to improve."
        )

    else:
        comments.append(
            "Several factors need attention before increasing training intensity."
        )

    return {
        "coach_comment": comments[0],
        "strengths": strengths,
        "risks": risks,
        "recommendations": recommendations,
    }