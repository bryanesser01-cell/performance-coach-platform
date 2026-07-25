from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from database.enums import (
    ExperienceLevel,
    InjuryStatus,
    Sex,
    Sport,
)


class AthleteBase(BaseModel):
    # -------------------------
    # Personal Information
    # -------------------------

    first_name: str = Field(
        ...,
        min_length=2,
        max_length=100,
    )

    last_name: str = Field(
        ...,
        min_length=2,
        max_length=100,
    )

    preferred_name: Optional[str] = Field(
        None,
        max_length=100,
    )

    date_of_birth: Optional[date] = None

    sex: Optional[Sex] = None

    # -------------------------
    # Physical Profile
    # -------------------------

    height_cm: Optional[float] = Field(
        None,
        gt=0,
        lt=300,
    )

    weight_kg: Optional[float] = Field(
        None,
        gt=0,
        lt=500,
    )

    # -------------------------
    # Sport Profile
    # -------------------------

    sport: Optional[Sport] = None

    primary_event: Optional[str] = Field(
        None,
        max_length=100,
    )

    experience_level: Optional[ExperienceLevel] = None

    years_training: Optional[int] = Field(
        None,
        ge=0,
        le=100,
    )

    # -------------------------
    # Training Profile
    # -------------------------

    weekly_training_days: Optional[int] = Field(
        None,
        ge=0,
        le=14,
    )

    weekly_training_hours: Optional[float] = Field(
        None,
        ge=0,
        le=100,
    )

    weekly_distance: Optional[float] = Field(
        None,
        ge=0,
        le=1000,
    )

    # -------------------------
    # Physiology
    # -------------------------

    resting_hr: Optional[int] = Field(
        None,
        ge=20,
        le=250,
    )

    threshold_hr: Optional[int] = Field(
        None,
        ge=20,
        le=250,
    )

    max_hr: Optional[int] = Field(
        None,
        ge=20,
        le=250,
    )

    ftp: Optional[int] = Field(
        None,
        ge=50,
        le=600,
    )

    vo2_max: Optional[float] = Field(
        None,
        ge=10,
        le=100,
    )

    # -------------------------
    # Health
    # -------------------------

    injury_status: Optional[InjuryStatus] = None

    # -------------------------
    # Coaching
    # -------------------------

    coach_notes: Optional[str] = Field(
        None,
        max_length=5000,
    )


class AthleteCreate(AthleteBase):
    pass


class AthleteUpdate(BaseModel):
    first_name: Optional[str] = Field(None, min_length=2, max_length=100)
    last_name: Optional[str] = Field(None, min_length=2, max_length=100)
    preferred_name: Optional[str] = Field(None, max_length=100)

    date_of_birth: Optional[date] = None
    sex: Optional[Sex] = None

    height_cm: Optional[float] = Field(None, gt=0, lt=300)
    weight_kg: Optional[float] = Field(None, gt=0, lt=500)

    sport: Optional[Sport] = None
    primary_event: Optional[str] = Field(None, max_length=100)
    experience_level: Optional[ExperienceLevel] = None
    years_training: Optional[int] = Field(None, ge=0, le=100)

    weekly_training_days: Optional[int] = Field(None, ge=0, le=14)
    weekly_training_hours: Optional[float] = Field(None, ge=0, le=100)
    weekly_distance: Optional[float] = Field(None, ge=0, le=1000)

    resting_hr: Optional[int] = Field(None, ge=20, le=250)
    threshold_hr: Optional[int] = Field(None, ge=20, le=250)
    max_hr: Optional[int] = Field(None, ge=20, le=250)

    ftp: Optional[int] = Field(None, ge=50, le=600)
    vo2_max: Optional[float] = Field(None, ge=10, le=100)

    injury_status: Optional[InjuryStatus] = None

    coach_notes: Optional[str] = Field(None, max_length=5000)


class AthleteResponse(AthleteBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int

    created_at: datetime
    updated_at: datetime
