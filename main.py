from datetime import datetime
import requests
import os
import pathlib
from urllib.parse import urlparse, urlsplit, unquote
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()
IMAGES_PATH = "images"
pathlib.Path('images/').mkdir(parents=True, exist_ok=True)


def download_image(image_url: str, path: str = f'{IMAGES_PATH}/image_{datetime.now()}.jpg', params: dict = None):
    response = requests.get(image_url, params=params)
    response.raise_for_status()
    binary_image = response.content
    with open(path, 'bw+') as file:
        file.write(binary_image)


def fetch_spacex_last_launch():
    api_method_url = 'https://api.spacexdata.com/v5/launches'
    spacex_response = requests.get(api_method_url)
    spacex_response.raise_for_status()
    flights = spacex_response.json()
    last_flight = None
    for flight in reversed(flights):
        if flight['links']['flickr']['original']:
            last_flight = flight
            break
    if last_flight:
        photo_links = last_flight['links']['flickr']['original']
        for i, link in enumerate(photo_links):
            download_image(link, f"{IMAGES_PATH}/spaceX_{i}.jpg")
    else:
        raise ValueError


def get_file_extension(image_url: str):
    path_only = unquote(urlparse(image_url).path)

    filename = os.path.split(path_only)[1]
    extension = os.path.splitext(path_only)[1]

    return filename, extension


def get_nasa_apod(count: int = 30):
    # APOD is the Astronomy Picture of the Day.
    api_method_url = 'https://api.nasa.gov/planetary/apod'
    request_params = {
        'api_key': os.getenv("NASA_API_KEY"),
        'count': count
    }
    nasa_response = requests.get(api_method_url, params=request_params)
    nasa_response.raise_for_status()
    apod_posts = nasa_response.json()
    for i, post in enumerate(apod_posts):
        download_image(post['url'], f"{IMAGES_PATH}/nasa_apod_{i}.jpg")


def get_nasa_epic(count: int = 5):
    # EPIC is the Earth Polychromatic Imaging Camera
    pass
    api_method_url = 'https://api.nasa.gov/EPIC/api/natural'
    api_archive_url = 'https://api.nasa.gov/EPIC/archive/natural'
    request_params = {
        'api_key': os.getenv("NASA_API_KEY"),
    }
    nasa_response = requests.get(f"{api_method_url}/images", request_params)
    nasa_response.raise_for_status()
    photo_cards = nasa_response.json()[:count]
    for i, card in enumerate(photo_cards):
        photo_date = datetime.strptime(card['date'], "%Y-%m-%d %H:%M:%S")
        photo_url = f"{api_archive_url}/{photo_date.year}/{photo_date.strftime('%m')}/{photo_date.strftime('%d')}/png/{get_file_extension(card['image'])[0]}.png".strip()
        download_image(photo_url, f"{IMAGES_PATH}/nasa_epic_{i}.png", params=request_params)


if __name__ == "__main__":
    get_nasa_epic()
