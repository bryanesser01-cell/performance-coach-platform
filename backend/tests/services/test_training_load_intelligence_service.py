from api.services.training_load_intelligence_service import (
    TrainingLoadIntelligenceService,
)


def test_empty_sessions():

    result = (
        TrainingLoadIntelligenceService()
        .analyse([])
    )

    assert result["risk"] == "unknown"


def test_insufficient_data():

    sessions = [
        {"training_load": 50}
        for _ in range(10)
    ]

    result = (
        TrainingLoadIntelligenceService()
        .analyse(sessions)
    )

    assert result["risk"] == "insufficient_data"

    assert result["acwr"] == 0.0


def test_low_risk():

    sessions = [
        {"training_load": 50}
        for _ in range(28)
    ]

    result = (
        TrainingLoadIntelligenceService()
        .analyse(sessions)
    )

    assert result["risk"] == "low"

    assert result["acwr"] == 1.0


def test_high_risk():

    # Older training (first 21 sessions)
    sessions = [
        {"training_load": 40}
        for _ in range(21)
    ]

    # Most recent week (last 7 sessions)
    sessions.extend(
        [
            {"training_load": 250}
            for _ in range(7)
        ]
    )

    result = (
        TrainingLoadIntelligenceService()
        .analyse(sessions)
    )

    assert result["risk"] == "high"

    assert result["acwr"] > 1.5
