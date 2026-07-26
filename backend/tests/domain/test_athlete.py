from datetime import date

import pytest

from domain.athlete.entities import Athlete


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

    assert athlete.age == (
        date.today().year - 2000 - ((date.today().month, date.today().day) < (1, 1))
    )
