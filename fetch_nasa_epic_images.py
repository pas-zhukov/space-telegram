"""

EPIC is the Earth Polychromatic Imaging Camera (NASA).
"""
import os
import requests
from datetime import datetime
from argparse import ArgumentParser
from img_functions import download_image, get_file_extension
from dotenv import load_dotenv


EPIC_API_METHOD_URL = "https://api.nasa.gov/EPIC/api/natural"
EPIC_ARCHIVE_URL = "https://api.nasa.gov/EPIC/archive/natural"


def main():
    load_dotenv()
    arg_parser = ArgumentParser(
        description='This program allows to download EPIC photos from NASA.'
    )
    arg_parser.add_argument(
        '-c',
        '--count',
        help="Count of EPIC photos to download. 10 by default.",
        default=10,
        type=int
    )
    args = arg_parser.parse_args()
    photos_count = args.count

    nasa_api_key = os.getenv("NASA_API_KEY")
    images_path = os.getenv("images_path")
    fetch_nasa_epic(nasa_api_key=nasa_api_key,
                    images_path=images_path,
                    photos_count=photos_count)


def fetch_nasa_epic(nasa_api_key: str,
                    images_path: str,
                    photos_count: int = 10):
    """

    Downloads a specified number of EPIC photos from NASA
    and saves them to a local directory.

    :param nasa_api_key: NASA API key, get it on https://api.nasa.gov/
    :param images_path: a path to a folder where images will be saved
    :param photos_count: the number of photos to download
    :return: None
    """
    request_params = {
        'api_key': nasa_api_key,
    }
    nasa_response = requests.get(f"{EPIC_API_METHOD_URL}/images",
                                 params=request_params)
    nasa_response.raise_for_status()
    photo_cards = nasa_response.json()[:photos_count]
    for index, photo_card in enumerate(photo_cards):
        photo_date = datetime.strptime(photo_card['date'], "%Y-%m-%d %H:%M:%S")
        photo_url = f"{EPIC_ARCHIVE_URL}/{photo_date.year}"\
                    f"/{photo_date.strftime('%m')}"\
                    f"/{photo_date.strftime('%d')}/png"\
                    f"/{get_file_extension(photo_card['image'])[0]}.png".strip()
        download_image(photo_url,
                       f"{images_path}/nasa_epic_{index}.png",
                       params=request_params)


if __name__ == "__main__":
    main()
