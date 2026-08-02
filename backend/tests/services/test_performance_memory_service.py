from api.services.performance_memory_service import (
    build_performance_memory,
    calculate_personal_best_status,
    generate_memory_coach_insight,
    store_training_response,
)


def test_personal_best_improvement():

    result = calculate_personal_best_status(
        current_result="4:58",
        previous_best="5:00",
    )

    assert result["personal_best_improved"] is True


def test_store_training_response():

    result = store_training_response(
        session_type="intervals",
        response="positive",
    )

    assert result["response"] == "positive"


def test_build_performance_memory():

    result = build_performance_memory(
        athlete_profile={
            "name": "Athlete",
        },
        race_results=[],
        training_history=[
            {
                "session_type": "intervals",
                "response": "positive",
            }
        ],
    )

    assert result["memory_ready"] is True


def test_memory_insight():

    result = generate_memory_coach_insight(
        {
            "performance_patterns": {
                "successful_sessions": [
                    "tempo",
                ],
                "difficult_sessions": [],
            }
        }
    )

    assert "tempo" in result["athlete_learning"]["responds_well_to"]
