from api.services.workout_recommendation_engine import (
    WorkoutRecommendationEngine,
)


class FakeTwin:

    def needs_recovery(self):
        return False

    def has_high_training_risk(self):
        return False

    def goal(self):
        return "5k"

    def race_phase(self):
        return "build"

    def is_improving(self):
        return True


def test_recommends_best_5k_workout():

    engine = WorkoutRecommendationEngine()

    result = engine.recommend(
        FakeTwin(),
    )

    assert result["workout"]["session_type"] in [
        "Threshold Run",
        "VO₂ Max Intervals",
    ]

    assert result["score"] > 0
