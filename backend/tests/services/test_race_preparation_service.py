from datetime import date

from api.services.race_preparation_service import (
    calculate_training_phase,
    generate_race_preparation_plan,
)


def test_base_phase():

    phase = calculate_training_phase(
        race_date=date(2027, 1, 1),
        current_date=date(2026, 1, 1),
    )

    assert phase == "base"


def test_peak_phase():

    phase = calculate_training_phase(
        race_date=date(2026, 8, 28),
        current_date=date(2026, 7, 28),
    )

    assert phase == "peak"


def test_taper_phase():

    phase = calculate_training_phase(
        race_date=date(2026, 8, 5),
        current_date=date(2026, 7, 28),
    )

    assert phase == "taper"


def test_generate_race_plan():

    result = generate_race_preparation_plan(
        race_date=date(2026, 8, 28),
        current_date=date(2026, 7, 28),
        target_time_seconds=1200,
    )

    assert result["target_time_seconds"] == 1200
    assert "training_phase" in result
