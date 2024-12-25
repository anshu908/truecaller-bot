import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "7916798453:AAGsAqqePGz5pqXqAFmmSu40tXfhG-7GHc8")
API_URL = "https://turecaller.pikaapis0.workers.dev/?number={}"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
