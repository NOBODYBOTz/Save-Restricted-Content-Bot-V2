# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25529076"))
API_HASH = getenv("API_HASH", "b8109a26ed1ba595aa5d70d0e38c3806")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "1715861188"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://avinashkakde646:avinashkakde646@cluster0.jlubkn6.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP = int(getenv("LOG_GROUP", ""))
FORCESUB = getenv("FORCESUB", "")
