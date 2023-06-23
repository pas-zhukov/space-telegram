import requests
from argparse import ArgumentParser
from img_functions import download_image
import global_vars_env


def main():
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

    fetch_spacex_launch_photos(launch_id=flight_id)


def get_last_flight_id() -> str:
    """

    This function retrieves the ID of the last SpaceX flight
    for which photos were taken and uploaded to Flickr.

    :return: None
    """
    spacex_response = requests.get(global_vars.SPACEX_API_METHOD_URL)
    spacex_response.raise_for_status()
    flights = spacex_response.json()
    last_flight = None
    for flight in reversed(flights):
        if flight['links']['flickr']['original']:
            last_flight = flight
            break
    return last_flight['id']


def fetch_spacex_launch_photos(launch_id: str):
    """

    Downloads images of a specific SpaceX launch from the SpaceX API
    and saves them to the local machine.

    :param launch_id:  ID of the SpaceX launch
    :return: None
    """
    spacex_response = requests.get(f"{global_vars.SPACEX_API_METHOD_URL}/{launch_id}")
    spacex_response.raise_for_status()
    flight_data = spacex_response.json()
    photo_links = flight_data['links']['flickr']['original']
    if flight_data:
        for i, link in enumerate(photo_links):
            download_image(link, f"{global_vars.IMAGES_PATH}/spaceX_{i}.jpg")
    else:
        raise ValueError("No photos were taken for this launch!")


if __name__ == "__main__":
    main()
