import os
import telebot
import random
from argparse import ArgumentParser
from img_functions import collect_photo_filenames
import global_vars_env


def main():
    arg_parser = ArgumentParser(
        description='This program allows to publish image in a Telegram channel.'
    )
    arg_parser.add_argument(
        '-p',
        '--image_path',
        help="Path to an image to publish. Picks random photo by default.",
        default=f"{global_vars_env.IMAGES_PATH}/{random.choice(collect_photo_filenames())}"
    )
    args = arg_parser.parse_args()
    image_path = args.image_path

    publish_photo(image_path)


def publish_photo(path: str):
    bot = telebot.TeleBot(global_vars_env.TG_BOT_TOKEN)
    with open(path, "rb") as file:
        bot.send_photo(global_vars_env.TG_CHANNEL_NAME, file)


if __name__ == "__main__":
    main()
