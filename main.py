import requests
import os
import random
import time
import urllib.parse
import telegram
from dotenv import load_dotenv


def download_image(url):
    response = requests.get(url)
    response.raise_for_status()
    path = urllib.parse.urlsplit(url).path.replace('/', '_')
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
    image_path = download_image(image_url)
    return image_path, image_comment


if __name__ == '__main__':
    load_dotenv()
    telegram_api_key = os.environ['TG_BOT_HTTP_KEY']
    bot = telegram.Bot(token=telegram_api_key)
    chat_id = os.environ['TG_CHANNEL_NAME']
    seconds_per_day = 86400

    while True:
        # get amount of comics
        last_comic_num = get_last_comic_num()
        # get random comic num
        rand_comic_num = random.randint(1, last_comic_num)
        # download comic
        image_path, image_comment = download_comic(rand_comic_num)
        # publish it
        with open(image_path, 'rb') as f:
            bot.send_photo(chat_id=chat_id, photo=f, caption=image_comment)
        # delete it
        os.remove(image_path)
        # wait till nex day
        time.sleep(seconds_per_day)
