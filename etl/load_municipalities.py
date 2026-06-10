from pathlib import Path

import pandas as pd
from sqlalchemy.orm import Session

from backend.database.session import SessionLocal
from backend.models.region import Region


FILE_PATH = (
    Path("data/processed/source/data_gaap/municipalities.xlsx")
)


def load_municipalities():

    print("Loading municipalities...")

    df = pd.read_excel(
        FILE_PATH,
        sheet_name="Onlineprodukt_Gemeinden30092025",
        header=4
    )

    municipalities = df[df.iloc[:, 0] == "60"]

    db: Session = SessionLocal()

    inserted = 0

    try:

        for _, row in municipalities.iterrows():

            state_code = str(int(row.iloc[2]))

            district_code = str(int(row.iloc[4]))

            municipality_code = str(int(row.iloc[6]))

            municipality_name = str(row.iloc[7]).strip()

            region = Region(
                state_code=state_code,
                district_code=district_code,
                municipality_code=municipality_code,
                municipality_name=municipality_name,
                region_type="municipality"
            )

            db.add(region)

            inserted += 1

            if inserted % 1000 == 0:
                print(f"Inserted {inserted}")

        db.commit()

        print(
            f"Municipality load complete. "
            f"Inserted={inserted}"
        )

    except Exception:

        db.rollback()
        raise

    finally:

        db.close()


if __name__ == "__main__":
    load_municipalities()