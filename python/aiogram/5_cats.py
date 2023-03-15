import time
import requests
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
DEBUG = config.get('DEFAULT', 'debug')
BOT_TOKEN = config.get('BOT', 'token')
API_URL: str = 'https://api.telegram.org/bot'
counter = 0

API_CAT_URL = 'https://aws.random.cat/meow'

error_text = 'picture with cat'
offset = -2

while counter < 100:
    print(f'{counter = }')
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    print(updates)
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CAT_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()['file']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else: 
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={error_text}')

    time.sleep(1)
    counter += 1