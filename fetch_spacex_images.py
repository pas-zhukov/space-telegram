import os

import requests
from argparse import ArgumentParser
from img_functions import download_image
from dotenv import load_dotenv


SPACEX_API_METHOD_URL = 'https://api.spacexdata.com/v5/launches'


def main():
    load_dotenv()
    arg_parser = ArgumentParser(
        description='This program allows to download photos from SpaceX rocket launches.'
    )
    arg_parser.add_argument(
        '-id',
        '--launch_id',
        help="ID of the SpaceX launch for which photos are to be downloaded. "
             "By default uses the last SpaceX flight "
             "for which photos were taken and uploaded to Flickr.",
        default=get_last_flight_id()
    )
    args = arg_parser.parse_args()
    flight_id = args.launch_id

    images_path = os.getenv("IMAGES_PATH")
    fetch_spacex_launch_photos(launch_id=flight_id, images_path=images_path)


def get_last_flight_id() -> str:
    """

    This function retrieves the ID of the last SpaceX flight
    for which photos were taken and uploaded to Flickr.

    :return: None
    """
    spacex_response = requests.get(SPACEX_API_METHOD_URL)
    spacex_response.raise_for_status()
    flights = spacex_response.json()
    last_flight = None
    for flight in reversed(flights):
        if flight['links']['flickr']['original']:
            last_flight = flight
            break
    return last_flight['id']


def fetch_spacex_launch_photos(launch_id: str, images_path: str):
    """

    Downloads images of a specific SpaceX launch from the SpaceX API
    and saves them to the local machine.

    :param launch_id:  ID of the SpaceX launch
    :param images_path: path to a folder where images will be saved
    :return: None
    """
    spacex_response = requests.get(f"{SPACEX_API_METHOD_URL}/{launch_id}")
    spacex_response.raise_for_status()
    flight = spacex_response.json()
    photo_links = flight['links']['flickr']['original']
    if photo_links:
        for i, link in enumerate(photo_links):
            download_image(link, f"{images_path}/spaceX_{i}.jpg")
    else:
        raise PhotosMissingError


class PhotosMissingError(ValueError):
    """

    Exception raised when no photos were taken for a SpaceX launch.
    """
    def __init__(self, message="No photos were taken for this launch!"):
        super().__init__(message)


if __name__ == "__main__":
    main()
