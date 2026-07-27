from schemas.analysis import PerformanceAnalysis
from schemas.workout import WorkoutRecommendation


def recommend_from_rules(
    analysis: PerformanceAnalysis,
) -> WorkoutRecommendation:

    # Beginner / Low Frequency

    if analysis.total_sessions < 3:
        return WorkoutRecommendation(
            workout_type="Easy Run",
            distance_km=8,
            duration_minutes=45,
            target_pace="Zone 2",
            target_heart_rate="Zone 2",
            purpose="Increase weekly training consistency.",
        )

    # Low Volume

    if analysis.total_distance < 25:
        return WorkoutRecommendation(
            workout_type="Aerobic Run",
            distance_km=10,
            duration_minutes=55,
            target_pace="Easy",
            target_heart_rate="Zone 2",
            purpose="Gradually build weekly running volume.",
        )

    # High Fatigue

    if analysis.total_training_load > 500:
        return WorkoutRecommendation(
            workout_type="Recovery Run",
            distance_km=6,
            duration_minutes=35,
            target_pace="Very Easy",
            target_heart_rate="Zone 1",
            purpose="Reduce accumulated fatigue.",
        )

    # Default

    return WorkoutRecommendation(
        workout_type="Threshold Run",
        distance_km=10,
        duration_minutes=50,
        target_pace="Threshold",
        target_heart_rate="Zone 4",
        purpose="Improve lactate threshold.",
    )
