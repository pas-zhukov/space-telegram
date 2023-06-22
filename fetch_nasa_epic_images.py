"""

EPIC is the Earth Polychromatic Imaging Camera (NASA).
"""

import os
import requests
from datetime import datetime
from argparse import ArgumentParser
from dotenv import load_dotenv
from functions import download_image, get_file_extension

load_dotenv()
IMAGES_PATH = os.getenv("IMAGES_PATH")
EPIC_API_METHOD_URL = "https://api.nasa.gov/EPIC/api/natural"
EPIC_ARCHIVE_URL = 'https://api.nasa.gov/EPIC/archive/natural'
NASA_API_KEY = os.getenv("NASA_API_KEY")


def main():
    arg_parser = ArgumentParser(
        description='This program allows to download EPIC photos from NASA.'
    )
    arg_parser.add_argument(
        '-c',
        '--count',
        help="Count of EPIC photos to download. 10 by default.",
        default=10
    )
    args = arg_parser.parse_args()
    try:
        photos_count = int(args.count)
        fetch_nasa_epic(photos_count=photos_count)
    except ValueError:
        print("Count parameter must be an integer!")


def fetch_nasa_epic(photos_count: int = 10):
    request_params = {
        'api_key': NASA_API_KEY,
    }
    nasa_response = requests.get(f"{EPIC_API_METHOD_URL}/images", params=request_params)
    nasa_response.raise_for_status()
    print(photos_count)
    print(len(nasa_response.json()))
    photo_cards = nasa_response.json()[:photos_count]
    for i, card in enumerate(photo_cards):
        photo_date = datetime.strptime(card['date'], "%Y-%m-%d %H:%M:%S")
        photo_url = f"{EPIC_ARCHIVE_URL}/{photo_date.year}/{photo_date.strftime('%m')}"\
                    f"/{photo_date.strftime('%d')}/png/"\
                    f"{get_file_extension(card['image'])[0]}.png".strip()
        print(photo_url)
        download_image(photo_url, f"{IMAGES_PATH}/nasa_epic_{i}.png", params=request_params)


if __name__ == "__main__":
    main()
