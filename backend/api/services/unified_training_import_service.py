from api.services.adapters.apple_health_adapter import (
    convert_apple_health_workout,
)
from api.services.adapters.coros_adapter import (
    convert_coros_activity,
)
from api.services.adapters.garmin_adapter import (
    convert_garmin_activity,
)
from api.services.adapters.manual_entry_adapter import (
    create_manual_training_entry,
)
from api.services.adapters.strava_adapter import (
    convert_strava_activity,
)


def select_adapter(
    source: str,
) -> str:
    """
    Identify adapter type.
    """

    supported = [
        "garmin",
        "apple_health",
        "coros",
        "strava",
        "manual",
    ]

    if source in supported:
        return source

    return "manual"


def import_training_session(
    source: str,
    raw_data: dict,
) -> dict:
    """
    Unified training import pipeline.

    Source
       ↓
    Adapter
       ↓
    Standard format
    """

    adapter = select_adapter(
        source,
    )

    if adapter == "garmin":

        session = convert_garmin_activity(
            raw_data,
        )

    elif adapter == "apple_health":

        session = convert_apple_health_workout(
            raw_data,
        )

    elif adapter == "coros":

        session = convert_coros_activity(
            raw_data,
        )

    elif adapter == "strava":

        session = convert_strava_activity(
            raw_data,
        )

    else:

        session = create_manual_training_entry(
            **raw_data,
        )

    return {
        "source": adapter,
        "training_session": session,
        "import_complete": True,
    }


def validate_import(
    import_record: dict,
) -> dict:
    """
    Validate unified import.
    """

    session = import_record.get(
        "training_session",
        {},
    )

    required_fields = [
        "distance_km",
        "duration_minutes",
        "session_type",
    ]

    missing = []

    for field in required_fields:

        if field not in session:

            missing.append(field)

    return {
        "valid": len(missing) == 0,
        "missing_fields": missing,
    }


def build_training_import_result(
    source: str,
    raw_data: dict,
) -> dict:
    """
    Complete import workflow.
    """

    record = import_training_session(
        source=source,
        raw_data=raw_data,
    )

    validation = validate_import(
        record,
    )

    return {
        "training_record": record,
        "validation": validation,
        "ready_for_coach": (validation["valid"]),
    }
