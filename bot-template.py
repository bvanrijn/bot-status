import telegram
import time
import requests
import asyncio

# TODO: change this to your own token
bot = telegram.Bot(token='123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11')
# TODO: change this name to something unique
dweet_name = "telegram-bot-ping"
dweet_base = "https://dweet.io/dweet/for/" + dweet_name + "?"

async def ping():
    while True:
        request = requests.get(dweet_base + "time=" + str(int(time.time())))
        time.sleep(30)

# TODO: build an awesome bot!

loop = asyncio.get_event_loop()  
loop.run_until_complete(ping())  
loop.close()
