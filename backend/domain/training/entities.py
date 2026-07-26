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

        if distance_km <= 0:
            raise ValueError("Distance must be greater than 0.")

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

    @property
    def average_speed_kmh(self) -> float:
        hours = self.duration_minutes / 60
        return self.distance_km / hours

    @property
    def formatted_pace(self) -> str:
        pace = self.pace_minutes_per_km
        minutes = int(pace)
        seconds = round((pace - minutes) * 60)
        return f"{minutes}:{seconds:02d}/km"
