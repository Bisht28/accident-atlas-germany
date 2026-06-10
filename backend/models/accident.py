from datetime import datetime

from sqlalchemy import BigInteger
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import func

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from backend.models.base import Base


class Accident(Base):
    __tablename__ = "accidents"

    accident_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    source_year: Mapped[int] = mapped_column(
        Integer,
        index=True
    )

    accident_year: Mapped[int] = mapped_column(
        Integer,
        index=True
    )

    accident_month: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    accident_hour: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    accident_weekday: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    region_id: Mapped[int | None] = mapped_column(
        ForeignKey("regions.region_id"),
        nullable=True,
        index=True
    )

    severity_category: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    accident_type: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    accident_subtype: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    is_bicycle: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    is_pedestrian: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    is_car: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    is_motorcycle: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    is_goods_vehicle: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    is_other_vehicle: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    latitude: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    longitude: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )