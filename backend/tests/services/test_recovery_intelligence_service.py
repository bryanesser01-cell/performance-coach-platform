from api.services.recovery_intelligence_service import (
    RecoveryIntelligenceService,
)


def test_calculate_recovery_score():

    service = RecoveryIntelligenceService()

    score = service.calculate_recovery_score(
        sleep_score=80,
        soreness_score=20,
        energy_score=90,
        motivation_score=70,
    )

    assert score == 80


def test_ready_status():

    service = RecoveryIntelligenceService()

    result = service.analyse(
        sleep_score=90,
        soreness_score=10,
        energy_score=90,
        motivation_score=90,
    )

    assert result["status"] == "ready"


def test_moderate_status():

    service = RecoveryIntelligenceService()

    result = service.analyse(
        sleep_score=70,
        soreness_score=40,
        energy_score=70,
        motivation_score=70,
    )

    assert result["status"] == "moderate"


def test_recovery_status():

    service = RecoveryIntelligenceService()

    result = service.analyse(
        sleep_score=40,
        soreness_score=80,
        energy_score=40,
        motivation_score=40,
    )

    assert result["status"] == "recovery"
