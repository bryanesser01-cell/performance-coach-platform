from unittest.mock import Mock, patch

from api.services.ai_coach_memory_context_service import (
    enrich_coach_prompt,
    get_ai_coach_memory_context,
    has_memory_context,
)


class MockMemory:
    def __init__(
        self,
        memory_type,
        memory_value,
    ):
        self.memory_type = memory_type
        self.memory_value = memory_value


@patch(
    "api.services.ai_coach_memory_context_service.recall",
)
def test_get_ai_coach_memory_context(
    mock_recall,
):
    mock_recall.return_value = [
        MockMemory(
            "goal",
            "Run sub 20 minute 5K",
        ),
    ]

    context = get_ai_coach_memory_context(
        db=Mock(),
        athlete_id=1,
    )

    assert context["goal"][0] == "Run sub 20 minute 5K"


@patch(
    "api.services.ai_coach_memory_context_service.get_ai_coach_memory_context",
)
def test_enrich_coach_prompt(
    mock_context,
):
    mock_context.return_value = {
        "goal": [
            "Improve 5K time",
        ],
    }

    result = enrich_coach_prompt(
        db=Mock(),
        athlete_id=1,
        question="Should I do intervals today?",
    )

    assert result["question"] == "Should I do intervals today?"

    assert result["memory_context"]["goal"][0] == "Improve 5K time"


def test_has_memory_context():

    context = {
        "memory_context": {
            "goal": [
                "Run faster",
            ],
        },
    }

    assert (
        has_memory_context(
            context,
        )
        is True
    )


def test_has_no_memory_context():

    context = {
        "memory_context": {},
    }

    assert (
        has_memory_context(
            context,
        )
        is False
    )
