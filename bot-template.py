# This script requires at least Python 3.5 because of asyncio
# This is the main bot script. You can start building on line 22

import telegram
import time
import requests
import asyncio

# TODO: Change this to your own bot token
bot = telegram.Bot(token='123456:YOU-BOT1234ghIkl-zyx57W2v1u123ew11')
# TODO: Change this name to something unique
dweet_name = "telegram-bot-ping"
dweet_base = "https://dweet.io/dweet/for/" + dweet_name + "?"

async def ping():
    while True:
        request = requests.get(dweet_base + "time=" + str(int(time.time())))
        print("Sent ping.")
        # Sleep for 2 minutes
        time.sleep(2 * 60)

# TODO: Build an awesome bot

loop = asyncio.get_event_loop()  
loop.run_until_complete(ping())  
loop.close()
