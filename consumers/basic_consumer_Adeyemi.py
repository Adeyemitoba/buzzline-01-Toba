"""
basic_consumer_Adeyemi.py

Read a log file as it is being written, designed for Adeyemi's specific use case.
"""

#####################################
# Import Modules
#####################################

# Import packages from Python Standard Library
import os
import time

# Import functions from local modules
from utils.utils_logger import logger, get_log_file_path

#####################################
# Define a function to process a single message
#####################################

def process_message(log_file) -> None:
    """
    Continuously read a log file and process each new message as it appears.

    Args:
        log_file (str): The path to the log file to read.
    """
    with open(log_file, "r") as file:
        # Start reading at the end of the file
        file.seek(0, os.SEEK_END)
        print("Adeyemi's consumer is ready and waiting for new log messages...")

        # Continuously monitor for new messages
        while True:
            line = file.readline()

            if not line:
                time.sleep(1)  # Delay to prevent busy looping
                continue

            message = line.strip()
            print(f"Adeyemi consumed a log message: {message}")

            if "I just loved a movie! It was funny." in message:
                alert_message = f"ALERT for Adeyemi: Special message detected! \n{message}"
                print(alert_message)
                logger.warning(alert_message)

#####################################
# Define main function for this script
#####################################

def main() -> None:
    """
    Main entry point for Adeyemi's consumer script.
    """
    logger.info("Adeyemi's consumer script STARTED...")

    log_file_path = get_log_file_path()
    logger.info(f"Adeyemi is reading from the file at {log_file_path}.")

    try:
        process_message(log_file_path)
    except KeyboardInterrupt:
        print("Adeyemi has stopped the process.")

    logger.info("Adeyemi's consumer script ENDED...")

#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    main()
