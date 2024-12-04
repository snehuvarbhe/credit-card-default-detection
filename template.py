import os  # For handling file and directory operations
from pathlib import Path  # For working with file paths in a platform-independent way
import logging  # For logging messages during execution

# Configure logging to display messages with a specific format
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the name of the project
project_name = 'default_detection'

# List of files to be created for the project structure
list_of_files = [
    f"src/{project_name}/__init__.py",                # Package initialization file for the project
    f"src/{project_name}/components/__init__.py",     # Package initialization file for 'components' module
    f"src/{project_name}/utils/__init__.py",          # Package initialization file for 'utils' module
    f"src/{project_name}/utils/common.py",            # Common utility functions
    f"src/{project_name}/config/__init__.py",         # Package initialization file for 'config' module
    f"src/{project_name}/config/configuration.py",    # Configuration-related code
    f"src/{project_name}/pipeline/__init__.py",       # Package initialization file for 'pipeline' module
    f"src/{project_name}/entity/__init__.py",         # Package initialization file for 'entity' module
    f"src/{project_name}/entity/config_entity.py",    # Entity definitions related to configuration
    f"src/{project_name}/constants/__init__.py",      # Package initialization file for 'constants' module
    "config/config.yaml",                             # YAML file for configuration
    "params.yaml",                                    # YAML file for parameter definitions
    "schema.yaml",                                    # YAML file for schema definitions
    "main.py",                                        # Main entry point of the project
    "app.py",                                         # Application entry point (e.g., for APIs)
    "requirements.txt",                               # File for listing Python dependencies
    "setup.py",                                       # Script for package setup
    "research/trials.ipynb",                          # Notebook for research and experimentation
    "templates/index.html"                            # HTML template file
]

# Loop through each file in the list
for filepath in list_of_files:
    # Convert the file path to a Path object for consistency
    filepath = Path(filepath)
    
    # Split the file path into directory and filename
    filedir, filename = os.path.split(filepath)
    
    # If the directory part of the path is not empty, create the directories
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # `exist_ok=True` ensures no error if the directory already exists
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    
    # If the file does not exist or is empty, create an empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:  # Using this command create a file 
            pass  # Create the file (it will be empty)
        logging.info(f"Creating empty file: {filepath}")
    else:
        # Log a message if the file already exists and is not empty
        logging.info(f"{filename} already exists.")
