from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field


# ---------------------------------------------------------------------------
# Reusable field definitions
# ---------------------------------------------------------------------------

Name = Annotated[str, Field(min_length=1, max_length=100)]

PositiveFloat = Annotated[float, Field(gt=0)]

PositiveInt = Annotated[int, Field(gt=0)]


# ---------------------------------------------------------------------------
# Base Schema
# ---------------------------------------------------------------------------

class AthleteBase(BaseModel):
    """
    Shared athlete fields.
    """

    name: Name

    age: int = Field(
        ...,
        ge=0,
        le=120,
    )

    height_cm: PositiveFloat

    weight_kg: PositiveFloat

    resting_hr: PositiveInt

    max_hr: PositiveInt

    sport: str = Field(
        ...,
        min_length=1,
        max_length=50,
    )

    primary_event: str = Field(
        ...,
        min_length=1,
        max_length=50,
    )

    experience_level: str | None = Field(
        default=None,
        max_length=50,
    )

    weekly_distance: float | None = Field(
        default=None,
        ge=0,
    )

    training_days_per_week: int | None = Field(
        default=None,
        ge=0,
        le=14,
    )

    current_5k_time: float | None = Field(
        default=None,
        gt=0,
    )

    injury_status: str | None = Field(
        default=None,
        max_length=100,
    )


# ---------------------------------------------------------------------------
# Create Schema
# ---------------------------------------------------------------------------

class AthleteCreate(AthleteBase):
    """
    Request body used to create an athlete.
    """


# ---------------------------------------------------------------------------
# Update Schema
# ---------------------------------------------------------------------------

class AthleteUpdate(BaseModel):
    """
    Request body used to update an athlete.
    """

    name: Name | None = None

    age: int | None = Field(
        default=None,
        ge=0,
        le=120,
    )

    height_cm: PositiveFloat | None = None

    weight_kg: PositiveFloat | None = None

    resting_hr: PositiveInt | None = None

    max_hr: PositiveInt | None = None

    sport: str | None = Field(
        default=None,
        min_length=1,
        max_length=50,
    )

    primary_event: str | None = Field(
        default=None,
        min_length=1,
        max_length=50,
    )

    experience_level: str | None = Field(
        default=None,
        max_length=50,
    )

    weekly_distance: float | None = Field(
        default=None,
        ge=0,
    )

    training_days_per_week: int | None = Field(
        default=None,
        ge=0,
        le=14,
    )

    current_5k_time: float | None = Field(
        default=None,
        gt=0,
    )

    injury_status: str | None = Field(
        default=None,
        max_length=100,
    )


# ---------------------------------------------------------------------------
# Response Schema
# ---------------------------------------------------------------------------

class AthleteResponse(AthleteBase):
    """
    Athlete returned by the API.
    """

    id: int

    model_config = ConfigDict(
        from_attributes=True,
    )


# ---------------------------------------------------------------------------
# Create Athlete Response
# ---------------------------------------------------------------------------

class AthleteCreateResponse(BaseModel):
    """
    Response returned after creating an athlete.
    """

    message: str

    athlete: AthleteResponse

    analysis: dict

    profile: dict