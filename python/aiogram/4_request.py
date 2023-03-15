from configparser import ConfigParser
import requests
from time import sleep

config = ConfigParser()
config.read('config.ini')
DEBUG = config.get('DEFAULT', 'debug')
BOT_TOKEN = config.get('BOT', 'token')

API_URL: str = 'https://api.telegram.org/bot'
TEXT: str = 'Вах'
max_counter: int = 100 

offset: int = -2
counter: int = 0
chat_id: int 


while counter < max_counter:
    print('attempt =', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

    sleep(1)
    counter += 1
