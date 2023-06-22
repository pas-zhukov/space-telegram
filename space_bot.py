import os

import telebot
from dotenv import load_dotenv
load_dotenv()

API_TOKEN = os.getenv("TG_BOT_TOKEN")

bot = telebot.TeleBot(API_TOKEN)
with open("images/spaceX_0.jpg", "rb") as file:
    bot.send_photo('@spacephotocards', file)