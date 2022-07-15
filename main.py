import os

import requests
from dotenv import load_dotenv

from download_image import download_image


def get_comics(comics_url):
    response = requests.get(comics_url)
    image_comics_url = response.json()["img"]
    file_name = "com.jpg"
    comment = response.json()["alt"]
    print(comment)
    download_image(image_comics_url, file_name)


def main():
    load_dotenv()
    client_id = os.environ["CLIENT_ID"]
    comics_url = "https://xkcd.com/1/info.0.json"
    get_comics(comics_url)

if __name__ == "__main__":
    main()