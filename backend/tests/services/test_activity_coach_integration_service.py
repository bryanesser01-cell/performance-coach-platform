from api.services.activity_coach_integration_service import (
    build_activity_coach_context,
    detect_training_risk,
    generate_activity_based_recommendation,
)


def test_build_activity_coach_context():

    activities = [
        {
            "training_stress": 50,
        },
        {
            "training_stress": 100,
        },
    ]

    result = build_activity_coach_context(
        activities,
    )

    assert (
        result["activity_count"]
        == 2
    )

    assert (
        result["total_training_stress"]
        == 150
    )


def test_detect_high_training_risk():

    result = detect_training_risk(
        {
            "total_training_stress": 600,
        }
    )

    assert (
        result["risk"]
        == "high"
    )


def test_generate_improving_recommendation():

    result = generate_activity_based_recommendation(
        {
            "fitness_trend": "improving",
            "total_training_stress": 100,
        }
    )

    assert (
        "progressive"
        in result["recommendation"]
    )


def test_generate_recovery_recommendation():

    result = generate_activity_based_recommendation(
        {
            "fitness_trend": "stable",
            "total_training_stress": 600,
        }
    )

    assert (
        "recovery"
        in result["recommendation"]
    )
