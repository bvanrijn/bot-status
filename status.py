# This script runs fine on both Python 2.7 and 3.5 and is the status bot script

import telegram
import time
import requests
import json

# TODO: change this to your own status bot token
bot = telegram.Bot(token='123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11')
# TODO: change this name to something unique
dweet_name = "telegram-bot-ping"
dweet = "https://dweet.io/get/latest/dweet/for/" + dweet_name

while True:
    ping = requests.get(dweet).content
    ping = json.loads(ping)

    # Yay! Success! We shall continue doing things
    if ping["this"] == "succeeded":
        # Get the last ping time
        last_ping = ping["with"][0]["content"]["time"]
        # 2 minutes without a ping.. It's probably just a hiccup.
        # FIXME: Refactor this code, but retain the same behaviour
        if time.time() - last_ping < 120:
            continue
        # Okay, it's been 5 minutes now. Let's send a message.
        elif time.time() - last_ping > 300:
            chat_id = bot.getUpdates()[-1].message.chat_id
            bot.sendMessage(chat_id=chat_id, text="More than 5 minutes since last ping")
        # FIXME: prevent from sending too many messages. One every hour should be enough
        # FIXME: calculate how much time has passed based on (time.time() - last_ping) / 60
        # TODO: Add more messages.... 1 hour, 12 hours, etc.
        # TODO: Add proper exception handling if needed
        else:
            continue

    time.sleep(30)
