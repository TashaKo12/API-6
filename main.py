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

def get_response_api(api_url, client_id, access_token):
    api_metod = "groups.get"
    metod_url = api_url.format(api_metod)

    params = {
        "access_token": access_token,
        "extended": 1,
        "v": 5.131
    }
    response = requests.get(metod_url, params=params)
    print(response.json())



def main():
    load_dotenv()
    client_id = os.environ["CLIENT_ID"]
    access_token = os.environ["ACCESS_TOKEN"]
    comics_url = "https://xkcd.com/1/info.0.json"
    api_url = "https://api.vk.com/method/{}"
    #get_comics(comics_url)
    get_response_api(api_url, client_id, access_token)


if __name__ == "__main__":
    main()