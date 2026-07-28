from unittest.mock import Mock

from api.services.athlete_memory_service import (
    build_memory_context,
    recall,
    recall_by_type,
    remember,
)


class MockMemory:
    def __init__(
        self,
        memory_type,
        memory_value,
    ):
        self.memory_type = memory_type
        self.memory_value = memory_value


def test_remember_creates_memory():

    db = Mock()

    result = remember(
        db=db,
        athlete_id=1,
        memory_type="goal",
        memory_value="Break 20 minute 5K",
    )

    assert result is not None


def test_recall_returns_athlete_memories():

    db = Mock()

    memories = recall(
        db=db,
        athlete_id=1,
    )

    assert memories is not None


def test_recall_by_type_returns_specific_memories():

    db = Mock()

    memories = recall_by_type(
        db=db,
        athlete_id=1,
        memory_type="goal",
    )

    assert memories is not None


def test_build_memory_context():

    memories = [
        MockMemory(
            "goal",
            "Run sub 20 minute 5K",
        ),
        MockMemory(
            "preference",
            "Prefers morning training",
        ),
        MockMemory(
            "race",
            "Australian Cross Country Championships",
        ),
    ]

    context = build_memory_context(
        memories,
    )

    assert (
        context["goal"][0]
        == "Run sub 20 minute 5K"
    )

    assert (
        context["preference"][0]
        == "Prefers morning training"
    )

    assert (
        context["race"][0]
        == "Australian Cross Country Championships"
    )
