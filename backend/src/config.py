import os
from dotenv import load_dotenv
load_dotenv()
API_VERSION = "v1"
SERVER_API_KEY = os.getenv("SERVER_API_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_DEPLOYMENT = os.getenv("AZURE_DEPLOYMENT")
AZURE_API_VERSION = os.getenv("API_VERSION")
PORT=5000
ERROR_MESSAGE = "Something went wrong. Please try again."
