import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_LINK = os.getenv("CHANNEL_LINK")
GROUP_LINK = os.getenv("GROUP_LINK")
ADD_ME_LINK = os.getenv("ADD_ME_LINK")
PORT = int(os.getenv("PORT", 8000))
