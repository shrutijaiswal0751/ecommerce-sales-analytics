
import json
from pathlib import Path

import pandas as pd


def main():
    # 1. Locate project folders
    project_root = Path(__file__).resolve().parents[2]
    raw_dir = project_root / "data" / "raw"
    processed_dir = project_root / "data" / "processed"

    # 2. Find the latest raw products file
    files = sorted(raw_dir.glob("products_*.json"))

    if not files:
        raise FileNotFoundError(
            "No products JSON file found in data/raw/"
        )

    raw_file = files[-1]

    # 3. Load the original JSON data
    with raw_file.open("r", encoding="utf-8") as file:
        data = json.load(file)

    products = data.get("products", [])

    if not products:
        raise ValueError("The products list is empty.")

    # 4. Convert JSON records into a DataFrame
    df = pd.DataFrame(products)

    print("Original rows and columns:", df.shape)

    # 5. Keep the selected 9 fields
    selected_columns = [
        "id",
        "title",
        "category",
        "price",
        "discountPercentage",
        "rating",
        "stock",
        "brand",
        "availabilityStatus",
    ]

    df = df[selected_columns].copy()

    # 6. Check data quality before making changes
    print("\nMissing values before cleaning:")
    print(df.isna().sum())

    print("\nDuplicate product IDs:", df["id"].duplicated().sum())

    # 7. Remove records without essential information
    df = df.dropna(subset=["id", "title", "category", "price"])

    # 8. Remove duplicate product IDs, if any
    df = df.drop_duplicates(subset=["id"], keep="first")

    # 9. Convert numeric fields to numeric data types
    numeric_columns = [
        "id",
        "price",
        "discountPercentage",
        "rating",
        "stock",
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # Remove records with invalid essential numeric values
    df = df.dropna(subset=["id", "price"])

    # 10. Save the processed dataset
    processed_dir.mkdir(parents=True, exist_ok=True)
    output_file = processed_dir / "products_cleaned.csv"

    df.to_csv(output_file, index=False, encoding="utf-8")

    # 11. Print summary
    print("\nRows and columns after cleaning:", df.shape)
    print("Remaining duplicate IDs:", df["id"].duplicated().sum())
    print("Processed file saved at:", output_file)
    print("\nPreview:")
    print(df.head())


if __name__ == "__main__":
    main()