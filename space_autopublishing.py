import time
from random import shuffle
from argparse import ArgumentParser
from space_bot_publish import publish_photo
from img_functions import collect_photo_filenames
import global_vars_env


def main():
    arg_parser = ArgumentParser(
        description='This program allows to publish images into a Telegram channel with specific interval.'
    )
    arg_parser.add_argument(
        '-d',
        '--delay',
        help="Frequency of posting images in hours. 4 hours by default.",
        default=4,
        type=float
    )
    args = arg_parser.parse_args()
    posting_delay = args.delay * 3600

    images = collect_photo_filenames()
    while True:
        for image in images:
            publish_photo(f"{global_vars_env.IMAGES_PATH}/{image}")
            time.sleep(posting_delay)
        shuffle(images)


if __name__ == "__main__":
    main()
