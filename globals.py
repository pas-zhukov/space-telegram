import os
import pathlib
from dotenv import load_dotenv


load_dotenv()


IMAGES_PATH = os.getenv("IMAGES_PATH")
pathlib.Path(f"{IMAGES_PATH}/").mkdir(parents=True, exist_ok=True)


NASA_API_KEY = os.getenv("NASA_API_KEY")


SPACEX_API_METHOD_URL = 'https://api.spacexdata.com/v5/launches'
EPIC_API_METHOD_URL = "https://api.nasa.gov/EPIC/api/natural"
EPIC_ARCHIVE_URL = 'https://api.nasa.gov/EPIC/archive/natural'
