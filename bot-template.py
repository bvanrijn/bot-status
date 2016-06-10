import telegram
import time
import requests

bot = telegram.Bot(token='123456789:YourBotToken')
dweet_name = "telegram-bot-ping"
dweet_base = "https://dweet.io/dweet/for/" + dweet_name + "?"

while True:
    request = requests.get(dweet_base + "time=" + str(int(time.time())))
    time.sleep(30)