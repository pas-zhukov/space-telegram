import os
import telebot
import random
from argparse import ArgumentParser
from img_functions import collect_photo_filenames
from dotenv import load_dotenv


def main():
    load_dotenv()
    arg_parser = ArgumentParser(
        description='This program allows to publish image in a Telegram channel.'
    )
    images_path = os.getenv("IMAGES_PATH")
    default_path = f"{images_path}"\
                   f"/{random.choice(collect_photo_filenames(images_path=images_path))}"
    arg_parser.add_argument(
        '-p',
        '--image_path',
        help="Path to an image to publish. Picks random photo by default.",
        default=default_path
    )
    args = arg_parser.parse_args()
    image_path = args.image_path

    tg_bot_token = os.getenv("TG_BOT_TOKEN")
    tg_channel_name = os.getenv("TG_CHANNEL_NAME")
    publish_photo(tg_bot_token, tg_channel_name, image_path)


def publish_photo(tg_bot_token: str, tg_channel_name: str, path: str):
    """

    Publishes a photo to a Telegram channel.

    :param tg_bot_token: The Telegram bot token.
    :param tg_channel_name: The name of the Telegram channel.
    :param path: The path to the photo to publish.
    """
    bot = telebot.TeleBot(tg_bot_token)
    with open(path, "rb") as file:
        bot.send_photo(tg_channel_name, file)


if __name__ == "__main__":
    main()
