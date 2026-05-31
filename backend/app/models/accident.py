from sqlalchemy import (
    Column,
    Integer,
    Float,
    ForeignKey
)
from sqlalchemy.orm import relationship

from app.core.database import Base


class Accident(Base):
    __tablename__ = "accidents"

    accident_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    year = Column(Integer, nullable=False, index=True)

    month = Column(Integer, nullable=True)

    hour = Column(Integer, nullable=True)

    weekday = Column(Integer, nullable=True)

    category = Column(Integer, nullable=True)

    type = Column(Integer, nullable=True)

    light = Column(Integer, nullable=True)

    ist_rad = Column(Integer, nullable=True)

    ist_pkw = Column(Integer, nullable=True)

    ist_fuss = Column(Integer, nullable=True)

    ist_krad = Column(Integer, nullable=True)

    ist_gkfz = Column(Integer, nullable=True)

    longitude = Column(Float, nullable=True)

    latitude = Column(Float, nullable=True)

    region_id = Column(
        Integer,
        ForeignKey("regions.region_id"),
        nullable=False,
        index=True
    )

    region = relationship("Region")