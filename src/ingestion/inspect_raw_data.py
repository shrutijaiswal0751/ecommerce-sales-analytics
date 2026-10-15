
import json
from pathlib import Path

# Project root directory
project_root = Path(__file__).resolve().parents[2]

# Raw data directory
raw_dir = project_root / "data" / "raw"

# Find the latest products JSON file
files = sorted(raw_dir.glob("products_*.json"))

if not files:
    print("No raw products file found.")
else:
    file_path = files[-1]

    with file_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    products = data.get("products", [])

    print("File:", file_path.name)
    print("Total products in file:", len(products))
    print("API total products:", data.get("total"))
    print("Available fields:")

    if products:
        print(list(products[0].keys()))

        print("\nFirst product:")
        print(json.dumps(products[0], indent=4))