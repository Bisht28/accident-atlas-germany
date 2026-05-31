from sqlalchemy import Column, Integer, String

from app.core.database import Base


class Indicator(Base):
    __tablename__ = "indicators"

    indicator_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    code = Column(
        String(50),
        unique=True,
        nullable=False
    )

    name = Column(
        String(255),
        nullable=False
    )

    unit = Column(
        String(50),
        nullable=True
    )

    source_system = Column(
        String(100),
        nullable=True
    )