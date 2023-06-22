import os
import time
from random import shuffle
from argparse import ArgumentParser
from dotenv import load_dotenv
from space_bot import publish_photo

load_dotenv()
IMAGES_PATH = os.getenv("IMAGES_PATH")


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
            publish_photo(f"{IMAGES_PATH}/{image}")
            time.sleep(posting_delay)
        shuffle(images)


def collect_photo_filenames(randomize: bool = False) -> list:
    """

    Collects the filenames of all the images
    present in the directory specified by the
    'IMAGES_PATH' variable and returns them as a list

    :param randomize: whether randomize images sequence or not
    :return: filenames of all the images present in the 'IMAGES_PATH' directory
    """
    images = None
    for _, _, files_list in os.walk(IMAGES_PATH):
        images = files_list
    if randomize:
        shuffle(images)
    return images


if __name__ == "__main__":
    main()
