from api.services.training_load_intelligence_service import (
    TrainingLoadIntelligenceService,
)


def test_calculate_acute_load():

    service = TrainingLoadIntelligenceService()

    activities = [
        {"training_stress": 120},
        {"training_stress": 80},
        {"training_stress": 100},
    ]

    assert (
        service.calculate_acute_load(
            activities,
        )
        == 300
    )


def test_calculate_chronic_load():

    service = TrainingLoadIntelligenceService()

    activities = [
        {"training_stress": 100},
        {"training_stress": 150},
        {"training_stress": 50},
    ]

    assert (
        service.calculate_chronic_load(
            activities,
        )
        == 300
    )


def test_calculate_acwr():

    service = TrainingLoadIntelligenceService()

    ratio = service.calculate_acwr(
        acute_load=300,
        chronic_load=400,
    )

    assert ratio == 0.75


def test_calculate_acwr_zero_chronic_load():

    service = TrainingLoadIntelligenceService()

    ratio = service.calculate_acwr(
        acute_load=300,
        chronic_load=0,
    )

    assert ratio == 0.0


def test_analyse():

    service = TrainingLoadIntelligenceService()

    activities = [
        {"training_stress": 100},
        {"training_stress": 150},
        {"training_stress": 50},
    ]

    result = service.analyse(
        activities,
    )

    assert result["acute_load"] == 300
    assert result["chronic_load"] == 300
    assert result["acwr"] == 1.0
    assert result["weekly_load"] == 300
    assert result["monthly_load"] == 300
    assert result["fatigue_score"] == 100.0


def test_calculate_weekly_load():

    service = TrainingLoadIntelligenceService()

    activities = [
        {"training_stress": 120},
        {"training_stress": 100},
        {"training_stress": 80},
    ]

    assert (
        service.calculate_weekly_load(
            activities,
        )
        == 300
    )


def test_calculate_monthly_load():

    service = TrainingLoadIntelligenceService()

    activities = [
        {"training_stress": 150},
        {"training_stress": 200},
        {"training_stress": 50},
    ]

    assert (
        service.calculate_monthly_load(
            activities,
        )
        == 400
    )


def test_calculate_fatigue_score():

    service = TrainingLoadIntelligenceService()

    fatigue = service.calculate_fatigue_score(
        acute_load=300,
        chronic_load=400,
    )

    assert fatigue == 75.0
