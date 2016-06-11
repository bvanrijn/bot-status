# This script runs fine on both Python 2.7 and 3.5 and is the status bot script

import telegram
import time
import requests
import json

# TODO: Change this to your own status bot token
bot = telegram.Bot(token='123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11')
# TODO: Change this name to something unique
dweet_name = "telegram-bot-ping"
dweet = "https://dweet.io/get/latest/dweet/for/" + dweet_name

while True:
    ping = requests.get(dweet).content
    ping = json.loads(ping)

    # Yay! Success! We shall continue doing things
    if ping["this"] == "succeeded":
        # Get the last ping time
        last_ping = ping["with"][0]["content"]["time"]
        # 5 minutes without a ping? Let's send an alert.
        if time.time() - last_ping > 5 * 60:
            print("More than 5 minutes since last ping. Please check on your bot.")
            chat_id = bot.getUpdates()[-1].message.chat_id
            bot.sendMessage(chat_id=chat_id, text="More than 10 minutes since last ping.\nPlease check on your bot.")
        # FIXME: Prevent from sending too many messages. One every hour should be enough
        # FIXME: Add proper exception handling
        # TODO:  Add more messages.... 1 hour, 12 hours, etc.
        else:
            print("All is well")
            continue

    # Sleep for 2.5 minutes
    time.sleep(2.5 * 60)
