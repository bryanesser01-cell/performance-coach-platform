from fastapi import APIRouter

from api.services.athlete_checkin_service import (
    create_checkin,
    generate_checkin_recommendation,
)

router = APIRouter(
    prefix="/athletes",
    tags=["Athlete Check-in"],
)


@router.post("/{athlete_id}/checkin")
def submit_checkin(
    athlete_id: int,
    energy: int,
    sleep_quality: int,
    soreness: int,
    motivation: int,
    notes: str | None = None,
):
    """
    Submit daily athlete check-in.
    """

    checkin = create_checkin(
        athlete_id=athlete_id,
        energy=energy,
        sleep_quality=sleep_quality,
        soreness=soreness,
        motivation=motivation,
        notes=notes,
    )

    checkin["recommendation"] = generate_checkin_recommendation(
        checkin["readiness_score"],
    )

    return checkin
