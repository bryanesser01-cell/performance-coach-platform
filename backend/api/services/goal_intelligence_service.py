"""
Goal Intelligence Service

Evaluates an athlete's progress towards their goals
and estimates the likelihood of achieving them.
"""


class GoalIntelligenceService:
    """
    Provides goal progress and confidence analysis.
    """

    def analyse(
        self,
        athlete_state: dict,
    ) -> dict:

        goals = athlete_state.get(
            "goals",
            [],
        )

        performance = athlete_state.get(
            "performance",
            {},
        )

        readiness = athlete_state.get(
            "readiness",
            {},
        )

        if not goals:
            return {
                "has_goal": False,
                "goal_status": "No active goals.",
                "confidence": 0,
                "on_track": False,
            }

        goal = goals[0]

        readiness_score = readiness.get(
            "score",
            0,
        )

        trend = performance.get(
            "trend",
            "unknown",
        )

        confidence = readiness_score

        if trend == "improving":
            confidence += 10
        elif trend == "declining":
            confidence -= 10

        confidence = max(
            0,
            min(
                100,
                confidence,
            ),
        )

        return {
            "has_goal": True,
            "goal": goal,
            "goal_status": ("On Track" if confidence >= 70 else "Needs Attention"),
            "confidence": confidence,
            "on_track": confidence >= 70,
        }
