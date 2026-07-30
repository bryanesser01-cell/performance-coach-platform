from api.services.training_load_service import (
    build_training_readiness_report,
    calculate_recovery_status,
    calculate_training_load,
)


def test_calculate_training_load():

    result = calculate_training_load(
        [
            {
                "duration_minutes": 40,
                "intensity": 2,
            },
            {
                "duration_minutes": 30,
                "intensity": 1,
            },
        ]
    )

    assert (
        result["training_load"]
        == 110
    )



def test_recovery_status():

    result = calculate_recovery_status(
        sleep_hours=5,
        fatigue_score=80,
        resting_hr_change=12,
    )

    assert (
        result["readiness"]
        == "REDUCE_TRAINING"
    )



def test_training_readiness_report():

    result = build_training_readiness_report(
        sessions=[],
        sleep_hours=8,
        fatigue_score=20,
        resting_hr_change=0,
    )

    assert (
        result["ready_to_train"]
        is True
    )
