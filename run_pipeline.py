
import subprocess
import sys
from pathlib import Path

# Project root folder
PROJECT_ROOT = Path(__file__).resolve().parent

# Pipeline steps in execution order
PIPELINE_STEPS = [
    ("API Ingestion", "src/ingestion/api_client.py"),
    ("Data Cleaning", "src/cleaning/clean_products.py"),
    ("Data Transformation", "src/transformation/clean_data.py"),
    ("PostgreSQL Loading", "src/database/load_to_postgres.py"),
]


def run_pipeline():
    print("Starting E-Commerce Sales Analytics Pipeline...\n")

    for step_name, script_path in PIPELINE_STEPS:
        full_path = PROJECT_ROOT / script_path

        print(f"\n--- Running: {step_name} ---")

        if not full_path.exists():
            print(f"ERROR: Script not found: {full_path}")
            sys.exit(1)

        result = subprocess.run(
            [sys.executable, str(full_path)],
            cwd=PROJECT_ROOT,
        )

        if result.returncode != 0:
            print(f"\nPipeline stopped: {step_name} failed.")
            sys.exit(result.returncode)

        print(f"Completed: {step_name}")

    print("\nPipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()
