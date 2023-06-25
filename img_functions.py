import os
from random import shuffle
from urllib.parse import urlparse, unquote
from datetime import datetime
import requests


def download_image(image_url: str,
                   path: str = f'images/image_{datetime.now()}.jpg',
                   params: dict = None):
    """

    This function downloads an image from a given URL
    and save it to a specified path on the local machine.

    :param image_url: the URL of the image to be downloaded
    :param path: the path where the downloaded image will be saved
    (default is a path with the current date and time in the filename,
    located in the "images/" directory)
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


def collect_photo_filenames(images_path: str, randomize: bool = False) -> list:
    """

    Collects the filenames of all the images
    present in the directory specified by the
    images_path argument and returns them as a list

    :param images_path: a path to images folder
    :param randomize: whether randomize images sequence or not
    :return: filenames of all the images present in the chosen directory
    """
    images = None
    for _, _, file_names in os.walk(images_path):
        images = file_names
    if not images:
        raise FileNotFoundError("Your IMAGES_PATH folder must contain at least one photo!")
    if randomize:
        shuffle(images)
    return images

