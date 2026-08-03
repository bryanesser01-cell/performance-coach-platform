from api.services.workout_scoring_engine import (
    WorkoutScoringEngine,
)


class FakeTwin:

    def __init__(
        self,
        recovery=False,
        risk=False,
        goal="5k",
        phase="build",
        improving=True,
    ):
        self._recovery = recovery
        self._risk = risk
        self._goal = goal
        self._phase = phase
        self._improving = improving

    def needs_recovery(self):
        return self._recovery

    def has_high_training_risk(self):
        return self._risk

    def goal(self):
        return self._goal

    def race_phase(self):
        return self._phase

    def is_improving(self):
        return self._improving


def test_recovery_state_prefers_easy_workout():

    engine = WorkoutScoringEngine()

    workout = {
        "session_type": "Recovery Run",
        "intensity": "very_easy",
    }

    result = engine.score_workout(
        workout=workout,
        twin=FakeTwin(
            recovery=True,
        ),
    )

    assert result["score"] > 0
    assert "Workout matches recovery needs." in result["reasons"]


def test_5k_vo2_scores_well():

    engine = WorkoutScoringEngine()

    workout = {
        "session_type": "VO₂ Max Intervals",
        "intensity": "very_hard",
    }

    result = engine.score_workout(
        workout=workout,
        twin=FakeTwin(
            goal="5k",
            phase="build",
        ),
    )

    assert result["score"] > 0
    assert any(
        "VO2 work supports 5K performance." in reason for reason in result["reasons"]
    )


def test_marathon_long_run_scores_well():

    engine = WorkoutScoringEngine()

    workout = {
        "session_type": "Long Run",
        "intensity": "easy",
    }

    result = engine.score_workout(
        workout=workout,
        twin=FakeTwin(
            goal="marathon",
            phase="base",
        ),
    )

    assert result["score"] > 0
    assert any(
        "Long run supports marathon development." in reason
        for reason in result["reasons"]
    )


def test_no_twin_returns_default_score():

    engine = WorkoutScoringEngine()

    result = engine.score_workout(
        workout={
            "session_type": "Threshold Run",
        },
        twin=None,
    )

    assert result["score"] == 50
