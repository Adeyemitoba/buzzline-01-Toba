"""
basic_producer_Adeyemi.py

Generate streaming buzz messages for Adeyemi's application.
"""

#####################################
# Import Modules
#####################################

# Import packages from Python Standard Library
import os
import random
import time

# Import external packages (must be installed in .venv first)
from dotenv import load_dotenv

# Import functions from local modules
from utils.utils_logger import logger

#####################################
# Load Environment Variables
#####################################

# Load environment variables from .env
load_dotenv()

#####################################
# Define Getter Functions for .env Variables
#####################################

def get_message_interval() -> int:
    """
    Fetch message interval from environment or use a default value.
    It returns an integer specifying how often to send messages.
    """
    interval = int(os.getenv("MESSAGE_INTERVAL_SECONDS", "3"))
    logger.info(f"Adeyemi's messages will be sent every {interval} seconds.")
    return interval

#####################################
# Define global variables
#####################################

ADJECTIVES = ["amazing", "funny", "boring", "exciting", "weird"]
ACTIONS = ["found", "saw", "tried", "shared", "loved"]
TOPICS = ["a movie", "a meme", "an app", "a trick", "a story"]

#####################################
# Define a function to generate buzz messages
#####################################

def generate_messages():
    """
    Continuously generate and yield buzz messages.
    """
    while True:
        adjective = random.choice(ADJECTIVES)
        action = random.choice(ACTIONS)
        topic = random.choice(TOPICS)
        yield f"I just {action} {topic}! It was {adjective}."

#####################################
# Define main() function to run this producer
#####################################

def main() -> None:
    """
    Main entry point for Adeyemi's producer script.
    """
    logger.info("Adeyemi's producer script STARTED...")
    interval_secs = get_message_interval()

    for message in generate_messages():
        logger.info(message)
        time.sleep(interval_secs)

    logger.info("Adeyemi's producer script ENDED...")

#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    main()
