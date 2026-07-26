from datetime import date

import pytest

from domain.athlete.entities import Athlete


def test_create_athlete_with_blank_first_name_raises_value_error():
    with pytest.raises(ValueError, match="First name cannot be blank."):
        Athlete.create(
            first_name="",
            last_name="Esser",
            date_of_birth=date(1981, 1, 1),
            sport="Running",
            height_cm=182,
            weight_kg=90.0,
        )


def test_create_athlete_with_blank_last_name_raises_value_error():
    with pytest.raises(ValueError, match="Last name cannot be blank."):
        Athlete.create(
            first_name="Bryan",
            last_name="",
            date_of_birth=date(1981, 1, 1),
            sport="Running",
            height_cm=182,
            weight_kg=90.0,
        )


def test_create_athlete_with_blank_sport_raises_value_error():
    with pytest.raises(ValueError, match="Sport cannot be blank."):
        Athlete.create(
            first_name="Bryan",
            last_name="Esser",
            date_of_birth=date(1981, 1, 1),
            sport="",
            height_cm=182,
            weight_kg=90.0,
        )


def test_create_athlete_with_invalid_height_raises_value_error():
    with pytest.raises(ValueError, match="Height must be greater than 0."):
        Athlete.create(
            first_name="Bryan",
            last_name="Esser",
            date_of_birth=date(1981, 1, 1),
            sport="Running",
            height_cm=0,
            weight_kg=90.0,
        )


def test_create_athlete_with_invalid_weight_raises_value_error():
    with pytest.raises(ValueError, match="Weight must be greater than 0."):
        Athlete.create(
            first_name="Bryan",
            last_name="Esser",
            date_of_birth=date(1981, 1, 1),
            sport="Running",
            height_cm=182,
            weight_kg=0,
        )


def test_athlete_age_returns_years():
    athlete = Athlete.create(
        first_name="Bryan",
        last_name="Esser",
        date_of_birth=date(2000, 1, 1),
        sport="Running",
    )

    expected_age = (
        date.today().year - 2000 - ((date.today().month, date.today().day) < (1, 1))
    )

    assert athlete.age == expected_age


def test_athlete_bmi_returns_expected_value():
    athlete = Athlete.create(
        first_name="Bryan",
        last_name="Esser",
        date_of_birth=date(2000, 1, 1),
        sport="Running",
        height_cm=182,
        weight_kg=90,
    )

    assert round(athlete.bmi, 1) == 27.2


def test_update_measurements_updates_height_and_weight():
    athlete = Athlete.create(
        first_name="Bryan",
        last_name="Esser",
        date_of_birth=date(2000, 1, 1),
        sport="Running",
        height_cm=182,
        weight_kg=90,
    )

    athlete.update_measurements(
        height_cm=185,
        weight_kg=82,
    )

    assert athlete.height_cm == 185
    assert athlete.weight_kg == 82
