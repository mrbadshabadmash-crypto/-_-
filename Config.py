import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH")
STRING_SESSION = os.getenv("STRING_SESSION")
MAX_DURATION_MINUTES = int(os.getenv("MAX_DURATION_MINUTES", 60))
AUTO_LEAVE_EMPTY_MINUTES = int(os.getenv("AUTO_LEAVE_EMPTY_MINUTES", 5))

DOWNLOAD_DIR = "downloads"
CACHE_DIR = "cache"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is required in .env file")
if API_ID == 0 or not API_HASH:
    raise ValueError("API_ID and API_HASH are required in .env file")
if not STRING_SESSION:
    raise ValueError("STRING_SESSION is required in .env file")
