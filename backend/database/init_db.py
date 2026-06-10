from backend.database.connection import engine

from backend.models import (
    Accident,
    ETLRun,
    Indicator,
    IndicatorValue,
    Region
)

from backend.models.base import Base


def create_tables():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
    print("GAAP tables created.")