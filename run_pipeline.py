
import subprocess
import sys
import logging
from pathlib import Path

# Project root folder
PROJECT_ROOT = Path(__file__).resolve().parent

# Log file path
LOG_FILE = PROJECT_ROOT / "pipeline.log"

# Logging configuration
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)

# Pipeline steps in execution order
PIPELINE_STEPS = [
    ("API Ingestion", "src/ingestion/api_client.py"),
    ("Data Cleaning", "src/cleaning/clean_products.py"),
    ("Data Transformation", "src/transformation/clean_data.py"),
    ("PostgreSQL Loading", "src/database/load_to_postgres.py"),
]


def run_pipeline():
    print("Starting E-Commerce Sales Analytics Pipeline...")
    logging.info("Pipeline started")

    for step_name, script_path in PIPELINE_STEPS:
        full_path = PROJECT_ROOT / script_path

        print(f"\n--- Running: {step_name} ---")
        logging.info("Started step: %s", step_name)

        if not full_path.exists():
            error_message = f"Script not found: {full_path}"
            print(f"ERROR: {error_message}")
            logging.error(error_message)
            sys.exit(1)

        try:
            result = subprocess.run(
                [sys.executable, str(full_path)],
                cwd=PROJECT_ROOT,
                check=True,
                text=True,
                capture_output=True,
            )

            if result.stdout:
                print(result.stdout, end="")
                logging.info("%s output:\n%s", step_name, result.stdout)

            if result.stderr:
                print(result.stderr, end="", file=sys.stderr)
                logging.warning("%s warnings/errors:\n%s", step_name, result.stderr)

            print(f"Completed: {step_name}")
            logging.info("Completed step: %s", step_name)

        except subprocess.CalledProcessError as error:
            error_message = (
                f"Pipeline stopped: {step_name} failed "
                f"with exit code {error.returncode}"
            )

            print(f"\n{error_message}")
            logging.error(error_message)

            if error.stdout:
                logging.error("Output:\n%s", error.stdout)

            if error.stderr:
                logging.error("Error details:\n%s", error.stderr)

            sys.exit(error.returncode)

    print("\nPipeline completed successfully!")
    logging.info("Pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()
