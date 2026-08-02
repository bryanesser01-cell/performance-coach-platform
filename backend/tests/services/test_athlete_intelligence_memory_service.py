from unittest.mock import Mock

from api.services.athlete_intelligence_memory_service import (
    build_athlete_intelligence_memory,
    generate_memory_intelligence_insight,
)


def test_build_athlete_intelligence_memory():

    memory = Mock()

    memory.memory_type = "goal"
    memory.memory_value = "Break 20 minute 5K"

    result = build_athlete_intelligence_memory(
        athlete_profile={
            "name": "Bryan",
        },
        stored_memories=[
            memory,
        ],
        race_results=[
            {
                "event": "5K",
                "time": "22:30",
            }
        ],
        training_history=[
            {
                "session_type": "threshold",
                "athlete_feedback": "strong",
                "response": "positive",
            }
        ],
    )

    assert result["intelligence_ready"] is True

    assert "goal" in result["memory_context"]


def test_generate_memory_intelligence_insight():

    result = generate_memory_intelligence_insight(
        {
            "training_patterns": {
                "responds_well_to": [
                    "threshold",
                ],
                "struggles_with": [],
            }
        }
    )

    assert "threshold" in result["strengths"]

    assert result["coach_message"] is not None
