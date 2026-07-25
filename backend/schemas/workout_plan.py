from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class WorkoutPlanBase(BaseModel):
    athlete_id: int
    title: str
    description: Optional[str] = None
    start_date: date
    end_date: Optional[date] = None
    goal: Optional[str] = None
    status: str = "Draft"


class WorkoutPlanCreate(WorkoutPlanBase):
    pass


class WorkoutPlanUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    goal: Optional[str] = None
    status: Optional[str] = None


class WorkoutPlanResponse(WorkoutPlanBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
