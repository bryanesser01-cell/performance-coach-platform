from dataclasses import dataclass
from datetime import date
from uuid import UUID, uuid4


@dataclass
class Athlete:
    """
    Core domain entity representing an athlete.

    This class contains business data only.
    It has no knowledge of databases, APIs, or frameworks.
    """

    id: UUID
    first_name: str
    last_name: str
    date_of_birth: date
    sport: str
    height_cm: float | None = None
    weight_kg: float | None = None
    active: bool = True

    @classmethod
    def create(
        cls,
        first_name: str,
        last_name: str,
        date_of_birth: date,
        sport: str,
        height_cm: float | None = None,
        weight_kg: float | None = None,
    ) -> "Athlete":
        first_name = first_name.strip()
        last_name = last_name.strip()
        sport = sport.strip()

        if not first_name:
            raise ValueError("First name cannot be blank.")

        if not last_name:
            raise ValueError("Last name cannot be blank.")

        if not sport:
            raise ValueError("Sport cannot be blank.")

        if height_cm is not None and height_cm <= 0:
            raise ValueError("Height must be greater than 0.")

        if weight_kg is not None and weight_kg <= 0:
            raise ValueError("Weight must be greater than 0.")

        return cls(
            id=uuid4(),
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            sport=sport,
            height_cm=height_cm,
            weight_kg=weight_kg,
            active=True,
        )

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self) -> int:
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (
                    self.date_of_birth.month,
                    self.date_of_birth.day,
                )
            )
        )

    @property
    def bmi(self) -> float:
        if self.height_cm is None or self.weight_kg is None:
            raise ValueError("Height and weight are required to calculate BMI.")

        height_m = self.height_cm / 100

        return self.weight_kg / (height_m**2)

    def update_measurements(
        self,
        *,
        height_cm: float,
        weight_kg: float,
    ) -> None:
        if height_cm <= 0:
            raise ValueError("Height must be greater than 0.")

        if weight_kg <= 0:
            raise ValueError("Weight must be greater than 0.")

        self.height_cm = height_cm
        self.weight_kg = weight_kg
