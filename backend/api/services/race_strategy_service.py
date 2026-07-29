def convert_time_to_seconds(
    time_string: str,
) -> int:
    """
    Convert race time string into seconds.

    Examples:
    4:45 -> 285
    20:00 -> 1200
    """

    parts = time_string.split(":")

    if len(parts) == 2:

        minutes = int(parts[0])
        seconds = int(parts[1])

        return (
            minutes * 60
            + seconds
        )

    return int(time_string)


def convert_seconds_to_time(
    seconds: int,
) -> str:
    """
    Convert seconds into MM:SS format.
    """

    minutes = seconds // 60

    remaining = seconds % 60

    return (
        f"{minutes}:{remaining:02d}"
    )


def calculate_split_time(
    total_seconds: int,
    distance: int,
    total_distance: int,
) -> int:
    """
    Calculate cumulative split time.
    """

    pace = (
        total_seconds
        / total_distance
    )

    return round(
        pace * distance,
    )


def get_race_checkpoints(
    event: str,
) -> list[int]:
    """
    Return race checkpoints.

    Uses cumulative distance markers.
    """

    event = event.lower()

    checkpoints = {

        "800m": [
            400,
            800,
        ],

        "1500m": [
            300,
            700,
            1100,
            1500,
        ],

        "mile": [
            409,
            809,
            1209,
            1609,
        ],

        "3000m": [
            400,
            800,
            1200,
            1600,
            2000,
            2400,
            2800,
            3000,
        ],

        "5000m": [
            1000,
            2000,
            3000,
            4000,
            5000,
        ],

        "10k": [
            1000,
            2000,
            3000,
            4000,
            5000,
            6000,
            7000,
            8000,
            9000,
            10000,
        ],

    }

    return checkpoints.get(
        event,
        [],
    )


def generate_race_strategy(
    event: str,
    target_time: str,
) -> dict:
    """
    Generate race split strategy
    from target race time.
    """

    checkpoints = get_race_checkpoints(
        event,
    )

    total_distance = (
        checkpoints[-1]
        if checkpoints
        else 0
    )

    total_seconds = convert_time_to_seconds(
        target_time,
    )

    splits = []

    for checkpoint in checkpoints:

        cumulative_seconds = (
            calculate_split_time(
                total_seconds,
                checkpoint,
                total_distance,
            )
        )

        splits.append(
            {
                "distance": checkpoint,
                "cumulative_time": (
                    convert_seconds_to_time(
                        cumulative_seconds,
                    )
                ),
            }
        )

    return {
        "event": event,
        "target_time": target_time,
        "checkpoints": splits,
    }


def generate_race_instruction(
    event: str,
) -> list[str]:
    """
    Generate race execution advice.
    """

    strategies = {

        "1500m": [
            "Control the first 300m.",
            "Settle into race rhythm.",
            "Increase effort after 1100m.",
            "Attack the final 300m.",
        ],

        "800m": [
            "Run controlled first 200m.",
            "Maintain position at 400m.",
            "Commit from 500m.",
            "Sprint home.",
        ],

        "5000m": [
            "Avoid going out too fast.",
            "Hold even pace.",
            "Increase effort in final kilometre.",
        ],

    }

    return strategies.get(
        event.lower(),
        [
            "Run controlled.",
            "Maintain target pace.",
            "Finish strongly.",
        ],
    )
