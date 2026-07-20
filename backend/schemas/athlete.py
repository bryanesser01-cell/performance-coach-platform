from pydantic import BaseModel, Field


class AthleteBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    age: int = Field(..., ge=5, le=100)

    height_cm: float = Field(..., gt=0)
    weight_kg: float = Field(..., gt=0)

    resting_hr: int = Field(..., ge=20, le=100)
    max_hr: int = Field(..., ge=100, le=240)

    sport: str = Field(..., min_length=2)
    primary_event: str = Field(..., min_length=2)

    experience_level: str = Field(..., min_length=2)
    weekly_distance: float = Field(..., ge=0)
    training_days_per_week: int = Field(..., ge=1, le=7)
    current_5k_time: float = Field(..., gt=0)
    injury_status: str = Field(..., min_length=2)


class AthleteCreate(AthleteBase):
    pass


class AthleteResponse(AthleteBase):
    id: int

    class Config:
        from_attributes = True