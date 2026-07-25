import datetime as dt

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    model_validator,
)

from database.enums import PerformanceCycleStatus


class PerformanceCycleBase(BaseModel):
    """
    Base schema for performance cycles.
    """

    title: str = Field(
        ...,
        min_length=1,
        max_length=100,
    )
    start_date: dt.date
    end_date: dt.date

    model_config = ConfigDict(
        str_strip_whitespace=True,
    )

    @model_validator(mode="after")
    def validate_dates(self):
        if self.end_date < self.start_date:
            raise ValueError("end_date must be on or after start_date")
        return self


class PerformanceCycleCreate(
    PerformanceCycleBase,
):
    """
    Schema for creating a performance cycle.
    """

    athlete_id: int
    status: PerformanceCycleStatus = PerformanceCycleStatus.PLANNED


class PerformanceCycleUpdate(BaseModel):
    """
    Schema for updating a performance cycle.
    """

    title: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )
    start_date: dt.date | None = None
    end_date: dt.date | None = None
    status: PerformanceCycleStatus | None = None

    model_config = ConfigDict(
        str_strip_whitespace=True,
    )

    @model_validator(mode="after")
    def validate_dates(self):
        if (
            self.start_date is not None
            and self.end_date is not None
            and self.end_date < self.start_date
        ):
            raise ValueError("end_date must be on or after start_date")
        return self


class PerformanceCycleResponse(BaseModel):
    """
    Schema returned for a performance cycle.
    """

    id: int
    athlete_id: int
    title: str
    start_date: dt.date
    end_date: dt.date
    status: PerformanceCycleStatus
    created_at: dt.datetime
    updated_at: dt.datetime

    model_config = ConfigDict(
        from_attributes=True,
    )
