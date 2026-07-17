from pydantic import BaseModel, Field


class AthleteCreate(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)

    age: int = Field(..., ge=5, le=100)

    height_cm: float = Field(..., gt=0)
    weight_kg: float = Field(..., gt=0)

    resting_hr: int = Field(..., ge=20, le=100)
    max_hr: int = Field(..., ge=100, le=240)

    sport: str = Field(..., min_length=2)
    primary_event: str = Field(..., min_length=2)
    experience_level: str = Field(..., min_length=2)