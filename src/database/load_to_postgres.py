
import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL


def main():
    project_root = Path(__file__).resolve().parents[2]
    load_dotenv(project_root / ".env")

    csv_file = project_root / "data" / "processed" / "products_cleaned.csv"

    if not csv_file.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_file}")

    required_settings = ["DB_HOST", "DB_PORT", "DB_NAME", "DB_USER", "DB_PASSWORD"]
    missing_settings = [
        key for key in required_settings if not os.getenv(key)
    ]

    if missing_settings:
        raise ValueError(
            f"Missing settings in .env: {', '.join(missing_settings)}"
        )

    df = pd.read_csv(csv_file)
    df.columns = df.columns.str.strip().str.lower()

    expected_columns = [
        "id", "title", "category", "price",
        "discountpercentage", "rating", "stock",
        "brand", "availabilitystatus"
    ]

    df = df[expected_columns]

    database_url = URL.create(
        drivername="postgresql+psycopg2",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        database=os.getenv("DB_NAME"),
    )

    engine = create_engine(database_url)

    try:
        with engine.begin() as connection:
            connection.execute(
                text("DELETE FROM public.products_transformed")
            )

            df.to_sql(
                "products_transformed",
                con=connection,
                schema="public",
                if_exists="append",
                index=False,
                method="multi",
            )

            database_rows = connection.execute(
                text("SELECT COUNT(*) FROM public.products_transformed")
            ).scalar()

        print("Data loaded successfully!")
        print("CSV rows:", len(df))
        print("Database rows:", database_rows)

    finally:
        engine.dispose()


if __name__ == "__main__":
    main()
