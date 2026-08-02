from api.services.training_load_intelligence_service import (
    TrainingLoadIntelligenceService,
)


def test_builds_training_load():

    sessions = [
        {
            "training_load": 100,
        }
        for _ in range(10)
    ]

    result = TrainingLoadIntelligenceService().analyse(
        sessions,
    )

    assert result["acute_load"] == 700
    assert result["risk"] == "insufficient_data"
    assert result["load_status"] == "building_history"
    assert result["recommendation"] == "collect_more_data"
    assert result["sufficient_history"] is False
