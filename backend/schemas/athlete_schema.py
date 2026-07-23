from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class AthleteBase(BaseModel):
    first_name: str
    last_name: str

    date_of_birth: Optional[date] = None
    sex: Optional[str] = None

    height_cm: Optional[float] = None
    weight_kg: Optional[float] = None

    ftp: Optional[int] = None
    threshold_hr: Optional[int] = None
    max_hr: Optional[int] = None
    resting_hr: Optional[int] = None


class AthleteCreate(AthleteBase):
    pass


class AthleteUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    date_of_birth: Optional[date] = None
    sex: Optional[str] = None

    height_cm: Optional[float] = None
    weight_kg: Optional[float] = None

    ftp: Optional[int] = None
    threshold_hr: Optional[int] = None
    max_hr: Optional[int] = None
    resting_hr: Optional[int] = None


class AthleteResponse(AthleteBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int

    created_at: datetime
    updated_at: datetime