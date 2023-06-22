import os
import telebot
import random
from argparse import ArgumentParser
from dotenv import load_dotenv
from img_functions import collect_photo_filenames

load_dotenv()
IMAGES_PATH = os.getenv("IMAGES_PATH")


def main():
    arg_parser = ArgumentParser(
        description='This program allows to publish image in a Telegram channel.'
    )
    arg_parser.add_argument(
        '-p',
        '--image_path',
        help="Path to an image to publish. Picks random photo by default.",
        default=f"{IMAGES_PATH}/{random.choice(collect_photo_filenames())}"
    )
    args = arg_parser.parse_args()
    image_path = args.image_path

    publish_photo(image_path)


def publish_photo(path: str):
    tg_bot_token = os.getenv("TG_BOT_TOKEN")
    tg_channel_name = os.getenv("TG_CHANNEL_NAME")
    bot = telebot.TeleBot(tg_bot_token)
    with open(path, "rb") as file:
        bot.send_photo(tg_channel_name, file)


if __name__ == "__main__":
    main()
