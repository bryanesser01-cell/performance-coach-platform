"""
Workout Scoring Engine

Scores candidate workouts based on athlete context.

Considers:

- Goal alignment
- Recovery status
- Training load risk
- Race phase
- Performance trend
"""


class WorkoutScoringEngine:
    """
    Scores workouts for suitability.
    """

    def score_workout(
        self,
        workout: dict,
        twin,
    ) -> dict:
        """
        Score a workout against athlete state.

        Returns:
            {
                "workout": workout,
                "score": int,
                "reasons": list
            }
        """

        score = 0
        reasons = []

        #
        # No Digital Twin
        #
        if twin is None:
            return {
                "workout": workout,
                "score": 50,
                "reasons": ["No athlete context available."],
            }

        #
        # Recovery suitability
        #
        if twin.needs_recovery():

            if workout.get("intensity") in [
                "very_easy",
                "easy",
            ]:
                score += 40
                reasons.append("Workout matches recovery needs.")

            else:
                score -= 30
                reasons.append("Workout intensity too high for recovery state.")

        else:

            score += 20
            reasons.append("Athlete is available for training.")

        #
        # Training risk
        #
        if twin.has_high_training_risk():

            if workout.get("intensity") == "easy":
                score += 20
                reasons.append("Easy intensity reduces training risk.")

            else:
                score -= 20
                reasons.append("High intensity conflicts with training risk.")

        #
        # Performance trend
        #
        if twin.is_improving():

            if workout.get("intensity") in [
                "moderate_hard",
                "hard",
            ]:
                score += 20
                reasons.append("Improving performance supports quality training.")

        #
        # Goal alignment
        #
        goal = twin.goal().lower()

        session_type = workout.get(
            "session_type",
            "",
        ).lower()

        if goal == "5k":

            if "threshold" in session_type:
                score += 15
                reasons.append("Threshold supports 5K development.")

            if "vo2" in session_type or "vo₂" in session_type:
                score += 15
                reasons.append("VO2 work supports 5K performance.")

        if goal == "marathon":

            if "long" in session_type:
                score += 15
                reasons.append("Long run supports marathon development.")

            if "tempo" in session_type:
                score += 10
                reasons.append("Tempo supports marathon strength.")

        #
        # Race phase
        #
        phase = twin.race_phase().lower()

        if phase == "taper":

            if "taper" in session_type:
                score += 30
                reasons.append("Workout matches taper phase.")

            else:
                score -= 20

        return {
            "workout": workout,
            "score": max(
                0,
                min(
                    score,
                    100,
                ),
            ),
            "reasons": reasons,
        }
