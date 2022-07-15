import requests

from download_image import download_image


def get_comics(comics_url):
    response = requests.get(comics_url)
    image_comics_url = response.json()["img"]
    file_name = "com.jpg"
    comment = response.json()["alt"]
    print(comment)
    download_image(image_comics_url, file_name)


def main():
    comics_url = "https://xkcd.com/1/info.0.json"
    get_comics(comics_url)

if __name__ == "__main__":
    main()