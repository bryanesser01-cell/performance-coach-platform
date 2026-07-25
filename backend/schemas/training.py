import datetime as dt

from pydantic import BaseModel, ConfigDict, Field


class TrainingSessionBase(BaseModel):
    athlete_id: int
    date: dt.date
    session_type: str = Field(..., min_length=1, max_length=100)
    distance: float = Field(..., ge=0)
    duration: float = Field(..., ge=0)
    average_pace: float = Field(..., ge=0)
    average_hr: int | None = Field(default=None, ge=20, le=250)
    max_hr: int | None = Field(default=None, ge=20, le=250)
    cadence: int | None = Field(default=None, ge=0, le=300)
    elevation_gain: float | None = Field(default=None, ge=0)
    training_load: float | None = Field(default=None, ge=0)
    rpe: int | None = Field(default=None, ge=1, le=10)
    notes: str | None = Field(default=None, max_length=5000)


class TrainingSessionCreate(TrainingSessionBase):
    pass


class TrainingSessionUpdate(BaseModel):
    date: dt.date | None = None
    session_type: str | None = Field(default=None, min_length=1, max_length=100)
    distance: float | None = Field(default=None, ge=0)
    duration: float | None = Field(default=None, ge=0)
    average_pace: float | None = Field(default=None, ge=0)
    average_hr: int | None = Field(default=None, ge=20, le=250)
    max_hr: int | None = Field(default=None, ge=20, le=250)
    cadence: int | None = Field(default=None, ge=0, le=300)
    elevation_gain: float | None = Field(default=None, ge=0)
    training_load: float | None = Field(default=None, ge=0)
    rpe: int | None = Field(default=None, ge=1, le=10)
    notes: str | None = Field(default=None, max_length=5000)


class TrainingSessionResponse(TrainingSessionBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: dt.datetime
    updated_at: dt.datetime
