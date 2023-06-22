import os
import telebot
from dotenv import load_dotenv

load_dotenv()
TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
TG_BOT_NAME = os.getenv("BOT_NAME")


def publish_photo(path: str):
    bot = telebot.TeleBot(TG_BOT_TOKEN)
    with open(path, "rb") as file:
        bot.send_photo(TG_BOT_NAME, file)


if __name__ == "__main__":
    from fetch_spacex_images import fetch_spacex_launch_photos, get_last_flight_id
    fetch_spacex_launch_photos(get_last_flight_id())
    publish_photo("images/spaceX_0.jpg")
