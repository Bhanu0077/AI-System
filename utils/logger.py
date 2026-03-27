# logger.py

import logging
import os

# Ensure log file is always created in project root
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "system.log")

def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers (important when re-running)
    if logger.hasHandlers():
        logger.handlers.clear()

    # File handler (UTF-8 safe)
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setLevel(logging.INFO)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Format
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    print("Logger initialized")
    print("Log file:", LOG_FILE)


def log(message):
    logging.info(message)