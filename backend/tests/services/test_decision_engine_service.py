from api.services.decision_engine_service import (
    DecisionEngineService,
)


def test_hard_session():

    service = DecisionEngineService()

    result = service.make_decision(
        recovery_status="ready",
        fatigue_score=60,
    )

    assert result["decision"] == "HARD_SESSION"
    assert result["confidence"] == 90
    assert "Recovery is high." in result["reason"]
    assert result["recommendation"] == ("Proceed with today's hard session.")


def test_easy_session():

    service = DecisionEngineService()

    result = service.make_decision(
        recovery_status="moderate",
        fatigue_score=60,
    )

    assert result["decision"] == "EASY_SESSION"
    assert result["confidence"] == 85
    assert result["recommendation"] == ("Complete an easy aerobic run.")


def test_rest_day():

    service = DecisionEngineService()

    result = service.make_decision(
        recovery_status="recovery",
        fatigue_score=95,
    )

    assert result["decision"] == "REST_DAY"
    assert result["confidence"] == 95
    assert result["recommendation"] == ("Prioritise recovery today.")
