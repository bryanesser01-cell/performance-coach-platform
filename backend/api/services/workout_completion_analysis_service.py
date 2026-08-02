def analyse_workout_completion(
    planned_workout: dict,
    athlete_feedback: dict,
) -> dict:
    """
    Analyse completed workout against athlete feedback.

    MVP version:
    - Uses athlete self-reported workout feedback
    - Produces coaching signals
    - Designed for future Garmin/Strava integration
    """

    completed = athlete_feedback.get(
        "completed",
        False,
    )

    rpe = athlete_feedback.get(
        "rpe",
        0,
    )

    target_hit = athlete_feedback.get(
        "target_hit",
        False,
    )

    difficulty = athlete_feedback.get(
        "difficulty",
        "unknown",
    )

    comments = athlete_feedback.get(
        "comments",
        "",
    )

    if not completed:
        return {
            "planned_workout": planned_workout,
            "execution_score": 0,
            "fatigue_signal": "unknown",
            "coach_signal": "RECOVERY_SESSION",
            "athlete_comments": comments,
            "summary": (
                "Workout was not completed. " "Focus on recovery and consistency."
            ),
        }

    execution_score = 100

    if not target_hit:
        execution_score -= 20

    if rpe >= 9:
        execution_score -= 20

    elif rpe >= 8:
        execution_score -= 10

    if difficulty == "very_hard":
        execution_score -= 10

    execution_score = max(
        execution_score,
        0,
    )

    if rpe >= 9:

        fatigue_signal = "high"

        coach_signal = "REDUCE_TRAINING"

        summary = (
            "Workout completed but "
            "high fatigue was detected. "
            "Training should be adjusted."
        )

    elif not target_hit:

        fatigue_signal = "moderate"

        coach_signal = "MAINTAIN_TRAINING"

        summary = "Workout completed but " "target performance was not achieved."

    else:

        fatigue_signal = "low"

        coach_signal = "PROGRESS_TRAINING"

        summary = "Workout completed successfully " "with good execution."

    return {
        "planned_workout": planned_workout,
        "execution_score": execution_score,
        "fatigue_signal": fatigue_signal,
        "coach_signal": coach_signal,
        "athlete_comments": comments,
        "summary": summary,
    }


def build_coach_feedback(
    workout_analysis: dict,
) -> str:
    """
    Convert workout analysis into
    athlete-friendly coach feedback.
    """

    return workout_analysis.get(
        "summary",
        "Workout analysed.",
    )
