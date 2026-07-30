from typing import Any


def normalise_training_session(
    source: str,
    raw_data: dict[str, Any],
) -> dict:
    """
    Convert different platform formats
    into the standard AI Coach format.

    Supported sources:
    - Garmin
    - Apple Health
    - COROS
    - Strava
    - Manual
    """

    if source == "garmin":

        return {
            "source": "garmin",
            "session_type": "run",

            "distance_km": (
                raw_data.get(
                    "distance_meters",
                    0,
                )
                / 1000
            ),

            "duration_minutes": (
                raw_data.get(
                    "duration_seconds",
                    0,
                )
                / 60
            ),

            "avg_heart_rate": raw_data.get(
                "average_hr"
            ),

            "cadence": raw_data.get(
                "cadence"
            ),
        }


    elif source == "apple_health":

        return {
            "source": "apple_health",
            "session_type": "run",

            "distance_km": raw_data.get(
                "distance_km",
                0,
            ),

            "duration_minutes": raw_data.get(
                "duration_minutes",
                0,
            ),

            "avg_heart_rate": raw_data.get(
                "heart_rate"
            ),

            "cadence": raw_data.get(
                "cadence"
            ),
        }


    elif source == "coros":

        return {
            "source": "coros",
            "session_type": "run",

            "distance_km": raw_data.get(
                "distance",
                0,
            ),

            "duration_minutes": raw_data.get(
                "time_minutes",
                0,
            ),

            "avg_heart_rate": raw_data.get(
                "hr_average"
            ),
        }


    elif source == "strava":

        return {
            "source": "strava",
            "session_type": "run",

            "distance_km": raw_data.get(
                "distance_km",
                0,
            ),

            "duration_minutes": raw_data.get(
                "moving_time_minutes",
                0,
            ),

            "avg_heart_rate": raw_data.get(
                "average_heartrate"
            ),
        }


    else:

        return {
            "source": "manual",
            "session_type": "run",

            "distance_km": raw_data.get(
                "distance_km",
                0,
            ),

            "duration_minutes": raw_data.get(
                "duration_minutes",
                0,
            ),

            "avg_heart_rate": raw_data.get(
                "avg_heart_rate"
            ),

            "cadence": raw_data.get(
                "cadence"
            ),
        }



def validate_training_data(
    training_session: dict,
) -> dict:
    """
    Validate standard training format.
    """

    required_fields = [
        "distance_km",
        "duration_minutes",
        "session_type",
    ]


    missing = []

    for field in required_fields:

        if field not in training_session:

            missing.append(field)


    return {
        "valid": len(missing) == 0,
        "missing_fields": missing,
    }



def identify_training_source(
    source: str,
) -> dict:
    """
    Identify connected platform.
    """

    supported_sources = [
        "garmin",
        "apple_health",
        "coros",
        "strava",
        "manual",
    ]


    return {
        "source": source,

        "supported": (
            source in supported_sources
        ),
    }



def build_training_import_record(
    source: str,
    raw_data: dict,
) -> dict:
    """
    Complete import pipeline.

    Source
       ↓
    Normalise
       ↓
    Validate
    """

    session = normalise_training_session(
        source=source,
        raw_data=raw_data,
    )


    validation = validate_training_data(
        session
    )


    return {
        "training_session": session,

        "validation": validation,

        "import_complete": (
            validation["valid"]
        ),
    }
