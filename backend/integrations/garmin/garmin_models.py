from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class GarminActivity:
    """
    Garmin activity received from Garmin Connect.

    This model is independent of SQLAlchemy and
    represents the raw activity data returned by
    the Garmin integration layer.
    """

    external_id: str

    athlete_id: int

    activity_type: str

    name: str

    started_at: datetime

    ended_at: datetime | None

    distance_m: float

    duration_s: float

    average_hr: int | None

    max_hr: int | None

    average_cadence: float | None

    elevation_gain_m: float | None

    calories: int | None

    source: str = "garmin"
