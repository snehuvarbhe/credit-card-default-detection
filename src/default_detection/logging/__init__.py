# Import necessary modules for logging and file handling
import os
import sys
import logging

# Define the log format with placeholders for timestamp, log level, module name, and message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s:]"

# Define the directory where log files will be stored
log_dir = "logs"

# Define the complete path to the log file inside the 'logs' directory
log_filepath = os.path.join(log_dir, "running_log.log")

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Set up the basic configuration for logging
logging.basicConfig(
    # Set the logging level to INFO, meaning messages at this level or higher will be logged
    level=logging.INFO,
    
    # Define the format of the log messages
    format=logging_str,
    
    # Define handlers for logging: one that writes to a file, and one that writes to the console (stdout)
    handlers=[
        logging.FileHandler(log_filepath),  # Log messages will also be written to the 'running_log.log' file
        logging.StreamHandler(sys.stdout)    # Log messages will also be printed to the console
    ]
)

# Create a logger object with the name "CCProjectlogger"
logger = logging.getLogger("CCProjectlogger")
