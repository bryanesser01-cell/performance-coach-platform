import datetime as dt

from pydantic import BaseModel, ConfigDict, Field


class GoalCreate(BaseModel):
    athlete_id: int
    target_distance: float = Field(..., gt=0)
    target_time_minutes: float = Field(..., gt=0)
    target_date: dt.date


class GoalUpdate(BaseModel):
    target_distance: float | None = Field(default=None, gt=0)
    target_time_minutes: float | None = Field(default=None, gt=0)
    target_date: dt.date | None = None


class GoalResponse(BaseModel):
    id: int
    athlete_id: int
    target_distance: float
    target_time_minutes: float
    target_date: dt.date
    created_at: dt.datetime
    updated_at: dt.datetime

    model_config = ConfigDict(from_attributes=True)


class GoalAnalysis(BaseModel):
    achievable: bool
    confidence: float
    estimated_completion_date: dt.date | None = None
    message: str


class GoalAnalysisResponse(BaseModel):
    goal: GoalResponse
    analysis: GoalAnalysis
