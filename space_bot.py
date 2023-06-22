import os

import telebot
from dotenv import load_dotenv
load_dotenv()

API_TOKEN = os.getenv("TG_BOT_TOKEN")

bot = telebot.TeleBot(API_TOKEN)

bot.send_message('@spacephotocards', 'HELL YEAH')