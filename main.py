import requests
import os
import random
import time
import urllib.parse
import telegram
from dotenv import load_dotenv


def download_image(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as f:
        f.write(response.content)
    return path


def get_last_comic_num():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['num']


def download_comic(comic_num):
    url = f'https://xkcd.com/{comic_num}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    image_url = response.json()['img']
    image_comment = response.json()['alt']
    image_path = urllib.parse.urlsplit(image_url).path.replace('/', '_')
    return image_url, image_path, image_comment


if __name__ == '__main__':
    load_dotenv()
    telegram_api_key = os.environ['TG_BOT_HTTP_KEY']
    bot = telegram.Bot(token=telegram_api_key)
    chat_id = os.environ['TG_CHANNEL_NAME']
    seconds_per_day = 86400

    while True:
        last_comic_num = get_last_comic_num()
        rand_comic_num = random.randint(1, last_comic_num)
        image_path = None
        try:
            image_url, image_path, image_comment = download_comic(
                rand_comic_num)
            download_image(image_url, image_path)
            with open(image_path, 'rb') as f:
                bot.send_photo(chat_id=chat_id, photo=f, caption=image_comment)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
        finally:
            os.remove(image_path)
            time.sleep(seconds_per_day)
