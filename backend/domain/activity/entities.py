from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID, uuid4

from .enums import (
    ActivityCategory,
    ActivitySource,
    ActivityStatus,
)


@dataclass
class Activity:
    """
    Core domain entity representing an athlete activity.

    This class intentionally contains only information about
    the activity itself.

    Performance metrics such as distance, heart rate, cadence,
    and pace belong in ActivityMetrics.
    """

    athlete_id: UUID

    category: ActivityCategory

    name: str

    started_at: datetime

    id: UUID = field(default_factory=uuid4)

    status: ActivityStatus = ActivityStatus.PLANNED

    source: ActivitySource = ActivitySource.MANUAL

    description: str | None = None

    external_id: str | None = None

    notes: str | None = None

    ended_at: datetime | None = None

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )