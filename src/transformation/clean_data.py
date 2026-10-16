
from pathlib import Path
import pandas as pd


def main():
    # Project ka main folder find karna
    project_root = Path(__file__).resolve().parents[2]

    # Cleaned data ki file ka path
    processed_file = (
        project_root / "data" / "processed" / "products_cleaned.csv"
    )

    if not processed_file.exists():
        raise FileNotFoundError(
            "Cleaned CSV not found. Please run clean_products.py first."
        )

    # Cleaned CSV ko read karna
    df = pd.read_csv(processed_file)

    print("Data loaded successfully!")
    print("Rows and columns:", df.shape)

    # Column names ko standard banana
    df.columns = df.columns.str.strip()

    # Text columns mein extra spaces remove karna
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].str.strip()

    # Brand ki missing values ko Unknown se fill karna
    if "brand" in df.columns:
        df["brand"] = df["brand"].fillna("Unknown")

    # Final data quality report
    print("\nMissing values after transformation:")
    print(df.isnull().sum())

    print("\nDuplicate product IDs:")
    print(df["id"].duplicated().sum())

    # Transformed data save karna
    df.to_csv(processed_file, index=False)

    print("\nTransformation completed!")
    print("File saved at:", processed_file)
    print("\nData preview:")
    print(df.head())


if __name__ == "__main__":
    main()
