from datetime import datetime

from pydantic import BaseModel, Field

from domain.activity.enums import (
    ActivityCategory,
    ActivitySource,
)


class ExternalActivityPayload(BaseModel):
    """
    Normalised payload received from external activity providers.

    Examples:
    - Garmin
    - Strava
    - COROS
    - Apple Health
    - FIT / GPX / TCX imports
    """

    source: ActivitySource

    external_id: str | None = None

    name: str = Field(
        min_length=1,
    )

    category: ActivityCategory

    started_at: datetime

    ended_at: datetime | None = None

    distance: float | None = None

    duration: float | None = None

    average_hr: int | None = None

    max_hr: int | None = None

    cadence: int | None = None

    elevation_gain: float | None = None
