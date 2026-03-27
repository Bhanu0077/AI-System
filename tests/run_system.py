# tests/run_system.py

from utils.logger import setup_logger, log
from core import run_pipeline

def main():
    setup_logger()

    input_data = {
        "query": "Tech products promotion",
        "platform": "Instagram",
        "budget": 50000,
        "audience": "students",
        "awareness": "High"
    }

    log("Running full system test...")

    result = run_pipeline(input_data)

    print("\n===== FINAL OUTPUT =====")
    print(result)


if __name__ == "__main__":
    main()