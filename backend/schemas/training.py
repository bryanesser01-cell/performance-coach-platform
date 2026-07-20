from pydantic import BaseModel


class TrainingSessionBase(BaseModel):
    athlete_id: int
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
    """Schema used when creating a training session."""
    pass


class TrainingSessionResponse(TrainingSessionBase):
    """Schema returned from the database/API."""
    id: int

    class Config:
        from_attributes = True