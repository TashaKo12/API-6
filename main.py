import os

import requests
from dotenv import load_dotenv

from download_image import download_image


def get_image_comics(comics_url):
    response = requests.get(comics_url)
    image_comics_url = response.json()["img"]
    file_name = "com.jpg"
    comment = response.json()["alt"]
    download_image(image_comics_url, file_name)


def check_key(api_url, access_token):
    api_metod = "groups.get"
    metod_url = api_url.format(api_metod)

    params = {
        "access_token": access_token,
        "extended": 1,
        "v": 5.131
    }
    response = requests.get(metod_url, params=params)
    response.raise_for_status()
    print(response.json())


def get_addresses_photos(api_url, access_token, client_id):
    api_metod = "photos.getWallUploadServer"
    metod_url = api_url.format(api_metod)
    params = {
        "access_token": access_token,
        "group_id": client_id,
        "v": 5.131
    }
    response = requests.get(metod_url, params=params)
    response.raise_for_status()
    return response.json()["response"]["upload_url"]


def upload_in_server(dowmload_adress_url, file_name="com.jpg"):
    with open(file_name, 'rb') as file:
        files={
            "photo": file
        }
        response = requests.post(dowmload_adress_url, files=files)
        response.raise_for_status()
    
    print(response.json())



def main():
    load_dotenv()
    client_id = os.environ["CLIENT_ID"]
    access_token = os.environ["ACCESS_TOKEN"]
    comics_url = "https://xkcd.com/1/info.0.json"
    api_url = "https://api.vk.com/method/{}"
    get_image_comics(comics_url)
    #check_key(api_url, access_token)
    dowmload_adress_url = get_addresses_photos(api_url, access_token, client_id)
    upload_in_server(dowmload_adress_url)
    


if __name__ == "__main__":
    main()