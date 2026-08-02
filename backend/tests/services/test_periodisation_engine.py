from api.services.periodisation_engine import (
    PeriodisationEngine,
)


def test_base_plan():

    result = PeriodisationEngine().build_plan(
        {
            "phase": "Base",
        }
    )

    assert result["weekly_focus"] == "Aerobic Development"

    assert result["volume"] == "High"


def test_build_plan():

    result = PeriodisationEngine().build_plan(
        {
            "phase": "Build",
        }
    )

    assert result["weekly_focus"] == "Threshold Development"


def test_peak_plan():

    result = PeriodisationEngine().build_plan(
        {
            "phase": "Peak",
        }
    )

    assert result["intensity"] == "High"


def test_taper_plan():

    result = PeriodisationEngine().build_plan(
        {
            "phase": "Taper",
        }
    )

    assert result["volume"] == "Low"


def test_unknown_phase():

    result = PeriodisationEngine().build_plan({})

    assert result["phase"] == "General Training"
