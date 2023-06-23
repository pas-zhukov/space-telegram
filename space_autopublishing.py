import time
from random import shuffle
from argparse import ArgumentParser
from space_bot_publish import publish_photo
from img_functions import collect_photo_filenames
import globals


def main():
    arg_parser = ArgumentParser(
        description='This program allows to publish images into a Telegram channel with specific interval.'
    )
    arg_parser.add_argument(
        '-d',
        '--delay',
        help="Frequency of posting images in hours. 4 hours by default.",
        default=4
    )
    args = arg_parser.parse_args()
    try:
        posting_delay = int(args.delay) * 3600
    except ValueError:
        try:
            posting_delay = float(args.delay) * 3600
        except ValueError:
            raise ValueError("Delay parameter must be an integer or float!")

    images = collect_photo_filenames()
    while True:
        for image in images:
            publish_photo(f"{globals.IMAGES_PATH}/{image}")
            time.sleep(posting_delay)
        shuffle(images)


if __name__ == "__main__":
    main()
