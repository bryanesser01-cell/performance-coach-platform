from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.services.activity_ingestion_service import (
    ingest_activity,
)
from database.session import get_db
from integrations.garmin import GarminActivityImporter
from integrations.strava import StravaActivityImporter

router = APIRouter(
    prefix="/activities",
    tags=["Activities"],
)


@router.post("/import")
def import_activity(
    payload: dict,
    db: Session = Depends(get_db),
):
    """
    Import activity from an external provider.

    Supported sources:
    - Garmin
    - Strava
    """

    source = payload.get("source")

    if source == "garmin":
        importer = GarminActivityImporter()

    elif source == "strava":
        importer = StravaActivityImporter()

    else:
        raise ValueError(
            "Unsupported activity source.",
        )

    return ingest_activity(
        db,
        importer,
        payload,
    )
