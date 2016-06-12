# Runs on:     Python 2.7 and Python 3.5
# Description: This is the status bot script. It runs on a different server

import telegram
import time
import requests
import json

# TODO: Change this to your own status bot token
bot = telegram.Bot(token='123456:STA-TUS1234ghIkl-zyx57W2v1u123ew11')
# TODO: Change this name to something unique
dweet_name = "telegram-bot-ping"
dweet = "https://dweet.io/get/latest/dweet/for/" + dweet_name
sentAlert = False

while True:
    ping = requests.get(dweet).json()
    # Yay! Success! We shall continue
    if ping["this"] == "succeeded":
        # Get the last ping time
        last_ping = ping["with"][0]["content"]["time"]
        # 5 minutes without a ping? Let's send an alert.
        if sentAlert == False and time.time() - last_ping > 5 * 60:
            print("More than 5 minutes since last ping. Please check on your bot.")
            chat_id = bot.getUpdates()[-1].message.chat_id
            bot.sendMessage(chat_id=chat_id, text="More than 10 minutes since last ping.\nPlease check on your bot.")
            sentAlert = True
        # FIXME: Fix having to restart the status script if the bot comes up again
        # TODO:  Find out if the above is true
        # TODO:  Add exception handling
        # TODO:  Add more messages.... 1 hour, 12 hours, etc.
        else:
            if sentAlert == True:
                print("Already sent an alert")
            else:
                print("All is probably well")

        # Send a message once every hour
        if sentAlert == True and time.time() - last_ping > 60 * 60:
            sentAlert == False

    # Sleep for 2 minutes and 30 seconds
    time.sleep(2.5 * 60)
