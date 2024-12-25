from flask import Flask, request
import requests

API_URL = "https://turecaller.pikaapis0.workers.dev/?number={}"
BOT_TOKEN = "7704975537:AAFDBD0l6gcEZXNQ1c1vRvo1DylJQL8F9yc"  # Replace with your bot token
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

app = Flask(__name__)  # Corrected this line

@app.route("/")
def home():
    return "Bot is running!"

@app.route(f"/webhook/{BOT_TOKEN}", methods=["POST"])
def webhook():
    """Handles incoming updates from Telegram."""
    update = request.get_json()

    # Check if the update is a message
    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "")

        if text == "/start":
            send_start_message(chat_id)
        elif text.startswith("+") and text[1:].isdigit():
            number_details = lookup_phone_number(text)
            send_message(chat_id, number_details)
        else:
            send_message(chat_id, "Invalid input. Please send a valid phone number.")
    
    # Handle inline button callbacks
    if "callback_query" in update:
        callback_query = update["callback_query"]
        chat_id = callback_query["message"]["chat"]["id"]
        data = callback_query["data"]

        if data == "faq":
            send_message(chat_id, "Here is the FAQ:\n1. Send /start to restart.\n2. Send a number to look it up.")
        elif data == "lookup":
            send_message(chat_id, "Please send a phone number to look up.")

    return "OK", 200


def send_start_message(chat_id):
    """Sends the /start message with inline buttons."""
    url = f"{TELEGRAM_API_URL}/sendMessage"
    reply_markup = {
        "inline_keyboard": [
            [
                {"text": "FAQ", "callback_data": "faq"},
                {"text": "Lookup a Number", "callback_data": "lookup"},
            ],
            [{"text": "Developer", "url": "https://t.me/Rishu1286"}],
        ]
    }
    payload = {"chat_id": chat_id, "text": "Welcome to the bot! Choose an option below:", "reply_markup": reply_markup}
    requests.post(url, json=payload)


def send_message(chat_id, text):
    """Sends a text message to the user."""
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)


def lookup_phone_number(number):
    """Fetches phone number details from the API."""
    try:
        response = requests.get(API_URL.format(number))
        if response.status_code == 200:
            data = response.json()
            return (
                f"Carrier: {data.get('carrier', 'Unknown')}\n"
                f"Country: {data.get('country', 'Unknown')}\n"
                f"International Format: {data.get('international_format', 'Unknown')}\n"
                f"Local Format: {data.get('local_format', 'Unknown')}\n"
                f"Location: {data.get('location', 'Unknown')}\n"
                f"Truecaller: {data.get('Truecaller', 'No name found')}\n"
                f"Unknown: {data.get('Unknown', 'Unknown')}"
            )
        else:
            return f"API Error: {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":  # Corrected this line
    app.run(host="0.0.0.0", port=5000)
