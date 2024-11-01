import telebot
import time
from datetime import datetime
import os
import schedule
import pytz
from keep_alive import keep_alive

keep_alive()

tz = pytz.timezone('Asia/Kathmandu')

def send_reminder():
    current_hour = datetime.now(tz).hour

    if 5 <= current_hour <= 22:
        try:
            bot.send_message(chat_id, "Time to drink some water! Stay hydrated 💧")
            print("Reminder sent!")
        except Exception as e:
            print(f"Failed to send message: {e}")

def job():
    send_reminder()

bot_token = os.environ.get('BOT_TOKEN')
chat_id = os.environ.get('CHAT_ID')

bot = telebot.TeleBot(bot_token)

schedule.every().hour.at(":00").do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
