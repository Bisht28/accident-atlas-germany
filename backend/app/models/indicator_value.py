from sqlalchemy import (
    Column,
    Integer,
    Float,
    ForeignKey
)

from app.core.database import Base


class IndicatorValue(Base):
    __tablename__ = "indicator_values"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    region_id = Column(
        Integer,
        ForeignKey("regions.region_id"),
        nullable=False
    )

    indicator_id = Column(
        Integer,
        ForeignKey("indicators.indicator_id"),
        nullable=False
    )

    year = Column(
        Integer,
        nullable=False
    )

    value = Column(
        Float,
        nullable=False
    )