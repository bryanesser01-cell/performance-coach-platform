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
