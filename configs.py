from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "0112234"))
    API_HASH = getenv("API_HASH", "abcdefg")
    BOT_TOKEN = getenv("BOT_TOKEN", "7916798453:AAGsAqqePGz5pqXqAFmmSu40tXfhG-7GHc8")
    CHID = int(getenv("CHID", "-1000112234"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    LOGCHID = int(getenv("LOGCHID", "-1000112234"))
    API = getenv("API", "abcdefu67-8dgdg")
cfg = Config()
