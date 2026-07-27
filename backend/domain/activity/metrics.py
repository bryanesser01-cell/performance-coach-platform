from __future__ import annotations

from dataclasses import dataclass

from .value_objects import Distance


@dataclass
class ActivityMetrics:
    """
    Immutable measurements captured during an activity.

    These are facts recorded by a device or entered manually.
    They should never contain AI-generated values.
    """

    distance: Distance | None = None

    duration_seconds: int | None = None

    average_heart_rate: int | None = None

    maximum_heart_rate: int | None = None

    average_cadence: int | None = None

    elevation_gain_metres: float | None = None

    calories: int | None = None

    average_power: int | None = None
