from unittest.mock import Mock

from api.services.athlete_memory_service import (
    build_memory_context,
    get_memory_summary,
    remember_performance,
    remember_race_result,
    remember_training_response,
)


def test_remember_performance():

    db = Mock()

    repository = Mock()

    db.repository = repository

    result = remember_performance(
        db,
        athlete_id=1,
        event="5K",
        previous_value="23:05",
        current_value="22:30",
    )

    assert result is not None


def test_remember_training_response():

    db = Mock()

    result = remember_training_response(
        db,
        athlete_id=1,
        training_block="Threshold Block",
        response="Improved aerobic capacity",
    )

    assert result is not None


def test_remember_race_result():

    db = Mock()

    result = remember_race_result(
        db,
        athlete_id=1,
        race="State Cross Country",
        result="Top 10 finish",
    )

    assert result is not None


def test_build_memory_context():

    memory_one = Mock()
    memory_one.memory_type = "goal"
    memory_one.memory_value = "Break 20 minutes for 5K"

    memory_two = Mock()
    memory_two.memory_type = "preference"
    memory_two.memory_value = "Prefers morning training"

    context = build_memory_context(
        [
            memory_one,
            memory_two,
        ]
    )

    assert context["goal"] == [
        "Break 20 minutes for 5K",
    ]

    assert context["preference"] == [
        "Prefers morning training",
    ]


def test_get_memory_summary():

    memory = Mock()

    memory.memory_type = "performance_improvement"
    memory.memory_value = "5K improved from 23:05 to 22:30"

    summary = get_memory_summary(
        [
            memory,
        ]
    )

    assert summary["memory_count"] == 1

    assert "performance_improvement" in summary["categories"]

    assert summary["memory_ready"] is True
