import telegram
import time
import requests
import asyncio

bot = telegram.Bot(token='123456789:YourBotToken')
dweet_name = "telegram-bot-ping"
dweet_base = "https://dweet.io/dweet/for/" + dweet_name + "?"

async def ping():
    while True:
        request = requests.get(dweet_base + "time=" + str(int(time.time())))
        time.sleep(30)

loop = asyncio.get_event_loop()  
loop.run_until_complete(ping())  
loop.close()
