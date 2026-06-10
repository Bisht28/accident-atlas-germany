from datetime import datetime

from sqlalchemy import BigInteger
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import func

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from backend.models.base import Base


class IndicatorValue(Base):
    __tablename__ = "indicator_values"

    value_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    indicator_id: Mapped[int] = mapped_column(
        ForeignKey("indicators.indicator_id"),
        index=True
    )

    region_id: Mapped[int] = mapped_column(
        ForeignKey("regions.region_id"),
        index=True
    )

    year: Mapped[int] = mapped_column(
        Integer,
        index=True
    )

    value: Mapped[float | None] = mapped_column(
        Numeric(20, 4),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )