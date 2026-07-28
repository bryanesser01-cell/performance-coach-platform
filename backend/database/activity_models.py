from sqlalchemy import Column, Float, ForeignKey, Integer

from database.base import Base


class ActivityMetric(Base):
    """
    Activity performance metrics database model.
    """

    __tablename__ = "activity_metrics"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    activity_id = Column(
        Integer,
        ForeignKey("activities.id"),
        nullable=False,
        index=True,
    )

    distance_km = Column(
        Float,
        nullable=True,
    )

    duration_seconds = Column(
        Float,
        nullable=True,
    )

    average_pace = Column(
        Float,
        nullable=True,
    )

    average_heart_rate = Column(
        Integer,
        nullable=True,
    )

    max_heart_rate = Column(
        Integer,
        nullable=True,
    )

    cadence = Column(
        Float,
        nullable=True,
    )

    elevation_gain = Column(
        Float,
        nullable=True,
    )

    calories = Column(
        Float,
        nullable=True,
    )

    training_load = Column(
        Float,
        nullable=True,
    )
