# Import the setuptools library, which is required for setting up the package
import setuptools

# Open the README file and read its content to use as long description
with open("README.md", "r", encoding="UTF-8") as f:
    long_description = f.read()

# Define the version of the package
__version__ = "0.0.0"

# Set the repository name and author details
REPO_NAME = "credit-card-default-detection"
AUTHOR_USER_NAME = "snehuvarbhe"
SRC_REPO = "default_detection"
AUTHOR_EMAIL = "snehuvarbhe26@gmail.com"

# Call the setuptools.setup function to specify package details
setuptools.setup(
    # The name of the package
    name=SRC_REPO,
    
    # Version of the package
    version=__version__,
    
    # Author's name
    author=AUTHOR_USER_NAME,
    
    # Author's email address
    author_email=AUTHOR_EMAIL,
    
    # Short description of the package
    description="A small python package for ml app",
    
    # Long description from the README file
    long_description=long_description,
    
    # The format for long description (Markdown in this case)
    long_description_content="text/markdown",
    
    # URL of the package's repository on GitHub
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    
    # Additional project URLs, like a bug tracker
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    
    # Directory structure where the source code is located
    package_dir={"": "src"},
    
    # Automatically find all packages under the "src" directory
    packages=setuptools.find_packages(where="src")
)
