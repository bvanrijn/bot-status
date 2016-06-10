import telegram
import time
import requests
import json

# TODO: change this to your own token
bot = telegram.Bot(token='123456789:StatusBotToken')
# TODO: change this name to something unique
dweet_name = "telegram-bot-ping"
dweet = "https://dweet.io/get/latest/dweet/for/" + dweet_name

while True:
    ping = requests.get(dweet).content
    ping = json.loads(ping)

    if ping["this"] == "succeeded":
        last_ping = int(ping["with"][0]["content"]["time"])
        if time.time() - last_ping < 120:
            continue
        elif time.time() - last_ping > 300:
            chat_id = bot.getUpdates()[-1].message.chat_id
            bot.sendMessage(chat_id=chat_id, text="More than 5 minutes since last ping")
        # TODO: Add more messages.... 1 hour, 12 hours, etc.
        # TODO: Add proper exception handling
        else:
            continue

    time.sleep(30)
