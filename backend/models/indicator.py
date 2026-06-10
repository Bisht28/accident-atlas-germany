from datetime import datetime

from sqlalchemy import BigInteger
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import func

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from backend.models.base import Base


class Indicator(Base):
    __tablename__ = "indicators"

    indicator_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    indicator_code: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True
    )

    indicator_name: Mapped[str] = mapped_column(
        String(255)
    )

    indicator_description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )