from api.services.coach_context_aggregator_service import (
    build_coach_context,
    generate_coach_context_summary,
    merge_training_intelligence,
)


def test_merge_training_intelligence():

    result = merge_training_intelligence(
        training_memory={
            "sessions": 5,
        },
        activity_context={
            "training_stress": 200,
        },
        recovery_context={
            "readiness_score": 80,
        },
        learning_memory={
            "confidence_adjustment": 20,
        },
    )

    assert (
        result["training"]["sessions"]
        == 5
    )

    assert (
        result["activity"]["training_stress"]
        == 200
    )


def test_build_coach_context():

    result = build_coach_context(
        athlete_id=1,
        athlete_state={
            "goal": "5K",
        },
        training_memory={
            "weekly_distance": 30,
        },
        learning_memory={
            "confidence_adjustment": 15,
        },
        activities=[
            {
                "training_stress": 100,
            },
        ],
        recovery_data={
            "readiness_score": 75,
        },
    )

    assert (
        result["athlete_id"]
        == 1
    )

    assert (
        "intelligence"
        in result
    )


def test_generate_context_summary():

    context = build_coach_context(
        athlete_id=1,
        activities=[
            {
                "training_stress": 100,
            },
        ],
        recovery_data={
            "readiness_score": 80,
        },
        learning_memory={
            "confidence_adjustment": 25,
        },
    )

    summary = generate_coach_context_summary(
        context,
    )

    assert (
        summary["readiness_score"]
        == 80
    )

    assert (
        summary["learning_confidence"]
        == 25
    )
