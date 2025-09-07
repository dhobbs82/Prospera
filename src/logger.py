"""
Logger for tracking events in each game execution.

Group Prospera
Authors: 

Brunner, John
Carrol, Josh
Hobbs, Derrick
Montgomery, Samuel
Reece, Manu
"""

import logging
from datetime import datetime
import os

# Ensure logs directory exists (optional, or you can log in root)
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Generate a unique filename based on current timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = os.path.join(LOG_DIR, f"snake_game_{timestamp}.log")

# Configure logger
logger = logging.getLogger("snake_game_logger")
logger.setLevel(logging.DEBUG)

# File handler
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(file_handler)

# Optional: console output
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
