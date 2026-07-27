from pydantic import BaseModel, Field


class GoalBase(BaseModel):
    athlete_id: int = Field(..., gt=0)

    goal_type: str = Field(..., min_length=2)

    target_value: float = Field(..., gt=0)

    target_unit: str = Field(..., min_length=1)

    current_value: float = Field(..., ge=0)

    status: str = Field(default="Active")


class GoalCreate(GoalBase):
    pass


class GoalResponse(GoalBase):
    id: int

    class Config:
        from_attributes = True


class GoalAnalysisResponse(BaseModel):
    progress_percent: float
    remaining: float
    remaining_unit: str
    status: str
    priority: str
    recommendations: list
