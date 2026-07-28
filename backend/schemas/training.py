from pydantic import BaseModel, ConfigDict, Field


class TrainingSessionBase(BaseModel):
    athlete_id: int = Field(..., gt=0)

    date: str

    session_type: str

    distance: float

    duration: float

    average_pace: float

    average_hr: int | None = None

    max_hr: int | None = None

    cadence: int | None = None

    elevation_gain: float | None = None

    training_load: float | None = None

    rpe: int | None = None

    notes: str | None = None


class TrainingSessionCreate(TrainingSessionBase):
    pass


class TrainingSessionResponse(TrainingSessionBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True,
    )
