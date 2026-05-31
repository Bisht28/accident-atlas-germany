from sqlalchemy import (
    Column,
    Integer,
    String
)

from app.core.database import Base


class SourceMetadata(Base):
    __tablename__ = "source_metadata"

    source_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    source_name = Column(
        String(255),
        nullable=False
    )

    source_url = Column(
        String(500),
        nullable=True
    )

    licence_name = Column(
        String(255),
        nullable=True
    )

    licence_url = Column(
        String(500),
        nullable=True
    )

    retrieved_date = Column(
        String(100),
        nullable=True
    )