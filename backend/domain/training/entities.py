from dataclasses import dataclass
from datetime import date
from uuid import UUID, uuid4


@dataclass
class TrainingSession:
    id: UUID
    athlete_id: UUID
    session_date: date
    session_type: str
    duration_minutes: int
    distance_km: float

    @classmethod
    def create(
        cls,
        athlete_id: UUID,
        session_date: date,
        session_type: str,
        duration_minutes: int,
        distance_km: float,
    ) -> "TrainingSession":
        if duration_minutes <= 0:
            raise ValueError("Duration must be greater than 0.")

        return cls(
            id=uuid4(),
            athlete_id=athlete_id,
            session_date=session_date,
            session_type=session_type,
            duration_minutes=duration_minutes,
            distance_km=distance_km,
        )

    @property
    def pace_minutes_per_km(self) -> float:
        return self.duration_minutes / self.distance_km
