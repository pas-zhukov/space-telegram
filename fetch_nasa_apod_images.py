"""

APOD is the Astronomy Picture of the Day (NASA).
"""

import os
import requests
from argparse import ArgumentParser
from dotenv import load_dotenv
from functions import download_image

load_dotenv()
IMAGES_PATH = os.getenv("IMAGES_PATH")
APOD_API_METHOD_URL = "https://api.nasa.gov/planetary/apod"
NASA_API_KEY = os.getenv("NASA_API_KEY")


def main():
    arg_parser = ArgumentParser(
        description='This program allows to download APOD photos from NASA.'
    )
    arg_parser.add_argument(
        '-c',
        '--count',
        help="Count of APOD photos to download. 10 by default.",
        default=10
    )
    args = arg_parser.parse_args()
    photos_count = args.count

    fetch_nasa_apod(photos_count=photos_count)


def fetch_nasa_apod(photos_count: int = 10):

    request_params = {
        'api_key': NASA_API_KEY,
        'count': photos_count
    }
    nasa_response = requests.get(APOD_API_METHOD_URL, params=request_params)
    nasa_response.raise_for_status()
    apod_posts = nasa_response.json()
    for i, post in enumerate(apod_posts):
        download_image(post['url'], f"{IMAGES_PATH}/nasa_apod_{i}.jpg")
