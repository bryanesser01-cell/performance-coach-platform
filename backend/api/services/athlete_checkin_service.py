from datetime import UTC, datetime


def create_checkin(
    athlete_id: int,
    energy: int,
    sleep_quality: int,
    soreness: int,
    motivation: int,
    notes: str | None = None,
) -> dict:
    """
    Create athlete daily check-in.
    """

    readiness_score = calculate_readiness_score(
        energy=energy,
        sleep_quality=sleep_quality,
        soreness=soreness,
        motivation=motivation,
    )

    return {
        "athlete_id": athlete_id,
        "energy": energy,
        "sleep_quality": sleep_quality,
        "soreness": soreness,
        "motivation": motivation,
        "readiness_score": readiness_score,
        "notes": notes,
        "created_at": datetime.now(UTC),
    }


def calculate_readiness_score(
    energy: int,
    sleep_quality: int,
    soreness: int,
    motivation: int,
) -> int:
    """
    Calculate athlete readiness score.

    Higher score = better readiness.
    """

    score = (
        energy
        + sleep_quality
        + motivation
        + (10 - soreness)
    ) / 4

    return round(score * 10)


def generate_checkin_recommendation(
    readiness_score: int,
) -> str:
    """
    Generate training recommendation.
    """

    if readiness_score >= 80:
        return (
            "Ready for quality training. "
            "Proceed with planned session."
        )

    if readiness_score >= 60:
        return (
            "Train as planned but monitor fatigue."
        )

    return (
        "Prioritise recovery and reduce intensity."
    )
