from etl.extract_zip import extract_all


def run():
    print("=" * 60)
    print("GAAP ETL START")
    print("=" * 60)

    extract_all()

    print("=" * 60)
    print("GAAP ETL COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    run()