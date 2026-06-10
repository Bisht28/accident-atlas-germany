from pathlib import Path

import pandas as pd

from backend.constants.region_levels import (
    STATE,
    REGBEZ,
    DISTRICT,
    MUNICIPALITY
)

from backend.database.session import SessionLocal
from backend.models.region import Region


FILE_PATH = Path(
    "data/processed/source/data_gaap/municipalities.xlsx"
)


def load_regions():

    print("Loading region hierarchy...")

    df = pd.read_excel(
        FILE_PATH,
        sheet_name="Onlineprodukt_Gemeinden30092025",
        header=4
    )

    db = SessionLocal()

    state_cache = {}
    regbez_cache = {}
    district_cache = {}
    municipality_cache = set()

    state_names = {}

    inserted_states = 0
    inserted_regbez = 0
    inserted_districts = 0
    inserted_municipalities = 0

    try:

        for _, row in df.iterrows():

            level = str(row.iloc[0])

            # -------------------------
            # STATE
            # -------------------------

            if level == "10":

                state_code = f"{int(row.iloc[2]):02d}"
                state_name = str(row.iloc[7]).strip()

                state_names[state_code] = state_name

            # -------------------------
            # DISTRICT
            # -------------------------

            elif level == "40":

                state_code = f"{int(row.iloc[2]):02d}"
                regbez_code = f"{int(row.iloc[3]):01d}"
                district_code = f"{int(row.iloc[4]):03d}"

                district_name = str(row.iloc[7]).strip()

                if state_code not in state_cache:

                    state = Region(
                        region_code=f"STATE_{state_code}",
                        source_code=state_code,
                        region_name=state_names[state_code],
                        region_level=STATE,
                        parent_region_id=None
                    )

                    db.add(state)
                    db.flush()

                    state_cache[state_code] = state

                    inserted_states += 1

                regbez_key = (
                    state_code +
                    regbez_code
                )

                if regbez_key not in regbez_cache:

                    regbez = Region(
                        region_code=f"REGBEZ_{regbez_key}",
                        source_code=regbez_key,
                        region_name=f"RegBez {regbez_code}",
                        region_level=REGBEZ,
                        parent_region_id=state_cache[
                            state_code
                        ].region_id
                    )

                    db.add(regbez)
                    db.flush()

                    regbez_cache[
                        regbez_key
                    ] = regbez

                    inserted_regbez += 1

                district_key = (
                    state_code +
                    regbez_code +
                    district_code
                )

                if district_key not in district_cache:

                    district = Region(
                        region_code=f"DISTRICT_{district_key}",
                        source_code=district_key,
                        region_name=district_name,
                        region_level=DISTRICT,
                        parent_region_id=regbez_cache[
                            regbez_key
                        ].region_id
                    )

                    db.add(district)
                    db.flush()

                    district_cache[
                        district_key
                    ] = district

                    inserted_districts += 1

            # -------------------------
            # MUNICIPALITY
            # -------------------------

            elif level == "60":

                state_code = f"{int(row.iloc[2]):02d}"
                regbez_code = f"{int(row.iloc[3]):01d}"
                district_code = f"{int(row.iloc[4]):03d}"
                group_code = f"{int(row.iloc[5]):04d}"
                municipality_code = f"{int(row.iloc[6]):03d}"

                municipality_name = str(
                    row.iloc[7]
                ).strip()

                # Skip special records
                if district_code == "000":
                    continue

                district_key = (
                    state_code +
                    regbez_code +
                    district_code
                )

                municipality_key = (
                    state_code +
                    regbez_code +
                    district_code +
                    group_code +
                    municipality_code
                )

                if municipality_key in municipality_cache:
                    continue

                municipality_cache.add(
                    municipality_key
                )

                # DEBUG SECTION
                if district_key not in district_cache:

                    print()
                    print("MISSING DISTRICT")
                    print("STATE:", state_code)
                    print("REGBEZ:", regbez_code)
                    print("DISTRICT:", district_code)
                    print("NAME:", municipality_name)
                    print("KEY:", district_key)

                    continue

                municipality = Region(
                    region_code=f"MUNI_{municipality_key}",
                    source_code=municipality_key,
                    region_name=municipality_name,
                    region_level=MUNICIPALITY,
                    parent_region_id=district_cache[
                        district_key
                    ].region_id
                )

                db.add(municipality)

                inserted_municipalities += 1

        db.commit()

        print()
        print(f"States={inserted_states}")
        print(f"RegBez={inserted_regbez}")
        print(f"Districts={inserted_districts}")
        print(f"Municipalities={inserted_municipalities}")

    except Exception:

        db.rollback()
        raise

    finally:

        db.close()


if __name__ == "__main__":
    load_regions()