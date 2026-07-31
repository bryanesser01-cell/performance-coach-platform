from datetime import date, timedelta

from api.services.race_intelligence_service import (
    RaceIntelligenceService,
)


def test_no_race():

    result = (
        RaceIntelligenceService()
        .analyse(None)
    )

    assert result["has_race"] is False

    assert (
        result["phase"]
        == "General Training"
    )


def test_base_phase():

    race = {
        "event": "Marathon",
        "priority": "A",
        "date": date.today() + timedelta(days=120),
    }

    result = (
        RaceIntelligenceService()
        .analyse(race)
    )

    assert result["phase"] == "Base"

    assert result["taper_required"] is False


def test_build_phase():

    race = {
        "event": "10K",
        "priority": "A",
        "date": date.today() + timedelta(days=56),
    }

    result = (
        RaceIntelligenceService()
        .analyse(race)
    )

    assert result["phase"] == "Build"


def test_peak_phase():

    race = {
        "event": "5K",
        "priority": "A",
        "date": date.today() + timedelta(days=21),
    }

    result = (
        RaceIntelligenceService()
        .analyse(race)
    )

    assert result["phase"] == "Peak"


def test_taper_phase():

    race = {
        "event": "Half Marathon",
        "priority": "A",
        "date": date.today() + timedelta(days=5),
    }

    result = (
        RaceIntelligenceService()
        .analyse(race)
    )

    assert result["phase"] == "Taper"

    assert result["taper_required"] is True
