from datetime import datetime

from sqlalchemy import BigInteger
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import func

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from backend.models.base import Base


class Region(Base):
    __tablename__ = "regions"

    region_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    region_code: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        index=True
    )

    source_code: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
        index=True
    )

    region_name: Mapped[str] = mapped_column(
        String(255),
        index=True
    )

    region_level: Mapped[str] = mapped_column(
        String(30),
        index=True
    )

    parent_region_id: Mapped[int | None] = mapped_column(
        ForeignKey("regions.region_id"),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    parent = relationship(
        "Region",
        remote_side=[region_id]
    )