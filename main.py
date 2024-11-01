import telebot
import time
from datetime import datetime
import os

bot_token = os.getenv('BOT_TOKEN')
chat_id = os.getenv('CHAT_ID')

bot = telebot.TeleBot(bot_token)

def send_reminder():
    current_hour = datetime.now().hour

    if 5 <= current_hour <= 22:
        bot.send_message(chat_id, "Time to drink some water! Stay hydrated 💧")

while True:
    print("Testing...")
    send_reminder()
    time.sleep(3600)
