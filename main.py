import requests

from download_image import download_image

url = "https://xkcd.com/1/info.0.json"

response = requests.get(url)
image_comics_url = response.json()["img"]
file_name = "com.jpg"

download_image(image_comics_url, file_name)
