from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Float
)
from sqlalchemy.orm import relationship

from app.core.database import Base


class Region(Base):
    __tablename__ = "regions"

    region_id = Column(Integer, primary_key=True, index=True)

    ags = Column(String(20), unique=True, nullable=False, index=True)

    name = Column(String(255), nullable=False)

    level = Column(String(50), nullable=False)

    parent_region_id = Column(
        Integer,
        ForeignKey("regions.region_id"),
        nullable=True
    )

    population = Column(Integer, nullable=True)

    area_km2 = Column(Float, nullable=True)

    longitude = Column(Float, nullable=True)

    latitude = Column(Float, nullable=True)

    parent = relationship(
        "Region",
        remote_side=[region_id]
    )