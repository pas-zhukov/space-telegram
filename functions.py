import os
from urllib.parse import urlparse, unquote
from datetime import datetime
import requests
from dotenv import load_dotenv
import pathlib

load_dotenv()
IMAGES_PATH = os.getenv("IMAGES_PATH")
pathlib.Path(f"{IMAGES_PATH}/").mkdir(parents=True, exist_ok=True)


def download_image(image_url: str,
                   path: str = f'{IMAGES_PATH}/image_{datetime.now()}.jpg',
                   params: dict = None):
    """

    This function downloads an image from a given URL
    and save it to a specified path on the local machine.

    :param image_url: the URL of the image to be downloaded
    :param path: the path where the downloaded image will be saved
    (default is a path with the current date and time in the filename,
    located in the IMAGES_PATH directory)
    :param params: optional parameters to be passed in the request
    :return: None
    """
    response = requests.get(image_url, params=params)
    response.raise_for_status()
    binary_image = response.content
    with open(path, 'bw+') as file:
        file.write(binary_image)


def get_file_extension(image_url: str) -> tuple[str, str]:
    """

    Returns the filename and extension of a file from a given URL.

    :param image_url: The URL of the file.
    :return: A tuple containing the filename and extension of the file.
    """
    path_only = unquote(urlparse(image_url).path)
    filename = os.path.split(path_only)[1]
    extension = os.path.splitext(path_only)[1]
    return filename, extension


if __name__ == "__main__":
    print(help(download_image))
    print(help(get_file_extension))
