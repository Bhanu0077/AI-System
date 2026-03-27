# test_log.py

from utils.logger import setup_logger, log

setup_logger()

log("System started")
log("Filtering influencers...")
log("Ranking completed")
log("Selected 3 influencers within budget")
log("Campaign performance updated")