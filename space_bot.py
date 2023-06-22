import os
import telebot
from dotenv import load_dotenv

load_dotenv()


def publish_photo(path: str):
    tg_bot_token = os.getenv("TG_BOT_TOKEN")
    tg_channel_name = os.getenv("TG_CHANNEL_NAME")
    bot = telebot.TeleBot(tg_bot_token)
    with open(path, "rb") as file:
        bot.send_photo(tg_channel_name, file)


if __name__ == "__main__":
    from fetch_spacex_images import fetch_spacex_launch_photos, get_last_flight_id
    fetch_spacex_launch_photos(get_last_flight_id())
    publish_photo("images/spaceX_0.jpg")
