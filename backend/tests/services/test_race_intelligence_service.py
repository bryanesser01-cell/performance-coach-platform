from datetime import date, timedelta

from api.services.race_intelligence_service import (
    RaceIntelligenceService,
)


def test_builds_race_intelligence():

    race = {
        "event": "5K Championship",
        "priority": "A",
        "date": date.today() + timedelta(days=14),
    }

    result = RaceIntelligenceService().analyse(
        race,
    )

    assert result["has_race"] is True
    assert result["goal_event"] == "5K Championship"
    assert result["phase"] == "Peak"
    assert result["recommendation"] == "maintain_peak"
    assert result["confidence"] == 1.0
