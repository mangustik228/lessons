from telethon import TelegramClient, events, sync, connection
from connection import api_hash, api_id
import os 

client = TelegramClient('tg_session', api_id, api_hash)
client.start()
path = 'media/example_5'

if not os.path.exists(path):
    os.makedirs(path)

for participant in client.get_participants('https://t.me/Parsinger_Telethon_Test'):
    for photo in client.iter_profile_photos(participant):
        client.download_media(photo, file=path)

result = 0
files = os.listdir(path)
for file in files:
    result += os.stat(f'{path}/{file}').st_size
print(f'Общее кол-во байт: {result}')

