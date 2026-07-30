from api.services.recovery_memory_integration_service import (
    build_recovery_coach_prompt_context,
    build_recovery_memory_context,
    enrich_coach_memory_with_recovery,
    generate_readiness_recommendation,
)


def test_build_recovery_memory_context():

    result = build_recovery_memory_context(
        {
            "readiness_score": 85,
        }
    )

    assert (
        result["readiness_score"]
        == 85
    )

    assert (
        result["recovery_status"]["status"]
        == "excellent"
    )


def test_low_readiness_context():

    result = build_recovery_coach_prompt_context(
        {
            "readiness_score": 30,
        }
    )

    assert (
        result["recovery_status"]
        == "poor"
    )


def test_recovery_added_to_memory():

    result = enrich_coach_memory_with_recovery(
        {
            "goal": "sub 20 minute 5K",
        },
        {
            "readiness_score": 70,
        },
    )

    assert (
        "recovery_memory"
        in result
    )


def test_generate_readiness_recommendation():

    result = generate_readiness_recommendation(
        {
            "readiness_score": 35,
        }
    )

    assert (
        "recovery"
        in result.lower()
    )
