"""

APOD is the Astronomy Picture of the Day (NASA).
"""

import os
import requests
from argparse import ArgumentParser
from dotenv import load_dotenv
from img_functions import download_image


APOD_API_METHOD_URL = "https://api.nasa.gov/planetary/apod"


def main():
    load_dotenv()
    arg_parser = ArgumentParser(
        description='This program allows to download APOD photos from NASA.'
    )
    arg_parser.add_argument(
        '-c',
        '--count',
        help="Count of APOD photos to download. 10 by default.",
        default=10,
        type=int
    )
    args = arg_parser.parse_args()
    photos_count = args.count

    nasa_api_key = os.getenv("NASA_API_KEY")
    images_path = os.getenv("images_path")
    fetch_nasa_apod(nasa_api_key=nasa_api_key, images_path=images_path, photos_count=photos_count)


def fetch_nasa_apod(nasa_api_key: str, images_path: str, photos_count: int = 10):
    """

    Downloads a specified number of Astronomy Picture of the Day (APOD) photos
    from NASA's API and save them to the local machine.

    :param nasa_api_key: NASA API key, get it on https://api.nasa.gov/
    :param images_path: a path to a folder where images will be saved
    :param photos_count: number of APOD photos to download (default is 10)
    :return: None
    """
    request_params = {
        'api_key': nasa_api_key,
        'count': photos_count
    }
    nasa_response = requests.get(APOD_API_METHOD_URL, params=request_params)
    nasa_response.raise_for_status()
    apod_posts = nasa_response.json()
    for i, post in enumerate(apod_posts):
        download_image(post['url'], f"{images_path}/nasa_apod_{i}.jpg")


if __name__ == "__main__":
    main()
