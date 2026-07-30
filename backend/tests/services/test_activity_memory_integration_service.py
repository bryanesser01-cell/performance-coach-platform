from api.services.activity_memory_integration_service import (
    build_activity_coach_prompt_context,
    build_activity_memory_context,
    enrich_coach_memory_with_activity,
)


def test_build_activity_memory_context():

    activities = [
        {
            "training_stress": 50,
        },
        {
            "training_stress": 100,
        },
    ]

    result = build_activity_memory_context(
        activities,
    )

    assert (
        result["activity_context"]
        ["total_training_stress"]
        == 150
    )


def test_activity_memory_added_to_context():

    activities = [
        {
            "training_stress": 100,
        },
    ]

    result = enrich_coach_memory_with_activity(
        {
            "goal": "sub 20 minute 5K",
        },
        activities,
    )

    assert (
        "activity_memory"
        in result
    )


def test_build_prompt_context():

    result = build_activity_coach_prompt_context(
        [
            {
                "training_stress": 200,
            },
        ],
    )

    assert (
        result["recent_activity_count"]
        == 1
    )

    assert (
        "training_risk"
        in result
    )
