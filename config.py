import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7954119369:AAEWZU-s1ygS2WjI4TEhIAJxP5yjspk_b-0")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28229153"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "b37046108ece20b5ed4fe74e563cabc2")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002347882407"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6514796890"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://ad-user-1:omE6Y7wN14da9HIQ@cluster0.zhqce.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002314782036"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "This Bot is used to get Links of Anime Files.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6514796890").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Join below Channel and press Try Again.\nThank you for your Support")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "Bot Uptime : <code>{uptime}</code>"
USER_REPLY_TEXT = None

ADMINS.append(OWNER_ID)
ADMINS.append(6514796890)

LOG_FILE_NAME = "filesbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
