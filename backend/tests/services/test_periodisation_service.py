from api.services.periodisation_service import (
    PeriodisationEngine,
)


def test_builds_periodisation():

    race_intelligence = {
        "phase": "Build",
    }

    result = PeriodisationEngine().build_plan(
        race_intelligence,
    )

    assert isinstance(result, dict)
    assert result["phase"] == "Build"
    assert result["weekly_focus"] == "Threshold Development"
    assert result["periodisation_complete"] is True
