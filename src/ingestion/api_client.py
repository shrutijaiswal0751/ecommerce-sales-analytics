import json
from datetime import datetime
from pathlib import Path

import requests


def fetch_products():
    url = "https://dummyjson.com/products"

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    return response.json()


def save_raw_data(data):
    # Project root directory
    project_root = Path(__file__).resolve().parents[2]

    # Raw data directory
    raw_dir = project_root / "data" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    # Date-based filename
    today = datetime.now().strftime("%Y-%m-%d")
    file_path = raw_dir / f"products_{today}.json"

    # Save the original API response as JSON
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"Raw data saved to: {file_path}")


def main():
    try:
        data = fetch_products()

        print("API request successful")
        print("Status code: 200")
        print("Products received:", len(data.get("products", [])))

        save_raw_data(data)

    except requests.RequestException as error:
        print("API request failed:", error)


if __name__ == "__main__":
    main()