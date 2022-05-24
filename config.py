import os
import re
from os import getenv

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "Avengers")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
START_MSG = os.environ.get("START_MSG", "<b>Hello {} 👋,\nI am a Music Downloader 😎\nI can Download songs from Spotify,JioSaavn, YouTube etc..\nCheck /help for more info</b>")
OWNER = os.environ.get("OWNER", "Peter Parker") 
msg = {}
