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
        return cls(
            id=uuid4(),
            first_name=first_name.strip(),
            last_name=last_name.strip(),
            date_of_birth=date_of_birth,
            sport=sport.strip(),
            height_cm=height_cm,
            weight_kg=weight_kg,
            active=True,
        )

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
