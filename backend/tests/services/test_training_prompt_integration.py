from api.services.coach_prompt_builder_service import (
    build_coach_prompt,
    has_training_memory,
)


def test_training_memory_added_to_prompt():

    prompt = build_coach_prompt(
        question="What should I train today?",
        athlete_state={
            "athlete": {
                "name": "Bryan",
                "primary_event": "5K",
            },
        },
        training_memory={
            "has_training_history": True,
            "training_history": [
                {
                    "type": "interval",
                    "focus": "5K speed",
                    "workout": (
                        "4 x 200m + 1 x 1km"
                    ),
                }
            ],
        },
    )

    assert (
        prompt["training_memory"]
        ["has_training_history"]
        is True
    )

    assert (
        prompt["training_memory"]
        ["training_history"][0]["type"]
        == "interval"
    )


def test_has_training_memory():

    context = {
        "training_memory": {
            "has_training_history": True,
        }
    }

    assert (
        has_training_memory(context)
        is True
    )
