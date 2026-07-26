from enum import Enum


class ActivityCategory(str, Enum):
    RUNNING = "running"
    STRENGTH = "strength"
    RECOVERY = "recovery"
    CYCLING = "cycling"
    SWIMMING = "swimming"
    WALKING = "walking"
    OTHER = "other"


class ActivityStatus(str, Enum):
    PLANNED = "planned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    SKIPPED = "skipped"
    CANCELLED = "cancelled"


class ActivitySource(str, Enum):
    MANUAL = "manual"
    GARMIN = "garmin"
    STRAVA = "strava"
    COROS = "coros"
    APPLE_HEALTH = "apple_health"
    FIT_IMPORT = "fit_import"
    GPX_IMPORT = "gpx_import"
    TCX_IMPORT = "tcx_import"