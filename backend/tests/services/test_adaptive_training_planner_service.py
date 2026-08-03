from api.services.adaptive_training_planner_service import (
    AdaptiveTrainingPlannerService,
)


def test_recovery_day_generates_recovery_session():

    planner = AdaptiveTrainingPlannerService()

    result = planner.generate_session(
        twin=None,
        decision="RECOVERY_DAY",
    )

    assert result["session_type"] == "Recovery Run"
    assert result["intensity"] == "very_easy"


def test_reduce_volume_generates_easy_run():

    planner = AdaptiveTrainingPlannerService()

    result = planner.generate_session(
        twin=None,
        decision="REDUCE_VOLUME",
    )

    assert result["session_type"] == "Easy Run"
    assert result["intensity"] == "easy"


def test_race_taper_generates_taper_session():

    planner = AdaptiveTrainingPlannerService()

    result = planner.generate_session(
        twin=None,
        decision="RACE_TAPER",
    )

    assert result["session_type"] == "Taper Session"


def test_progress_training_generates_quality_session():

    planner = AdaptiveTrainingPlannerService()

    result = planner.generate_session(
        twin=None,
        decision="PROGRESS_TRAINING",
    )

    assert result["session_type"] == "Threshold Run"
    assert result["intensity"] == "moderate_hard"


def test_maintain_plan_generates_aerobic_run():

    planner = AdaptiveTrainingPlannerService()

    result = planner.generate_session(
        twin=None,
        decision="MAINTAIN_PLAN",
    )

    assert result["session_type"] == "Easy Run"
    assert result["duration_minutes"] == 45


def test_digital_twin_recovery_overrides_decision():

    class FakeTwin:

        def needs_recovery(self):
            return True

        def is_tapering(self):
            return False

    planner = AdaptiveTrainingPlannerService()

    result = planner.generate_session(
        twin=FakeTwin(),
        decision="PROGRESS_TRAINING",
    )

    assert result["session_type"] == "Recovery Run"


def test_digital_twin_taper_session():

    class FakeTwin:

        def needs_recovery(self):
            return False

        def is_tapering(self):
            return True

    planner = AdaptiveTrainingPlannerService()

    result = planner.generate_session(
        twin=FakeTwin(),
        decision="PROGRESS_TRAINING",
    )

    assert result["session_type"] == "Taper Session"
