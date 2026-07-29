from api.services.coach_prompt_builder_service import (
    build_coach_prompt,
    generate_prompt_summary,
    has_voice_memory,
)


def test_build_coach_prompt_contains_context():

    result = build_coach_prompt(
        question="Should I train today?",
        athlete_state={
            "athlete": {
                "name": "Bryan",
                "primary_event": "5K",
            },
            "readiness": {
                "score": 85,
            },
        },
        memory_context={
            "goal": "Run sub 20 minute 5K",
        },
        voice_memory_context={
            "has_history": True,
        },
        coach_decision={
            "decision": "progress_training",
        },
    )

    assert (
        result["question"]
        == "Should I train today?"
    )

    assert (
        result["voice_memory"]["has_history"]
        is True
    )

    assert (
        result["coach_decision"]["decision"]
        == "progress_training"
    )


def test_generate_prompt_summary():

    context = {
        "athlete_state": {
            "athlete": {
                "name": "Bryan",
                "primary_event": "5K",
            },
            "readiness": {
                "score": 85,
            },
        }
    }

    summary = generate_prompt_summary(
        context,
    )

    assert (
        "Bryan"
        in summary
    )

    assert (
        "85"
        in summary
    )


def test_has_voice_memory():

    context = {
        "voice_memory": {
            "has_history": True,
        }
    }

    assert (
        has_voice_memory(
            context,
        )
        is True
    )
