from telethon import TelegramClient, sync, connection, events
from telethon.tl.types import InputMessagesFilterPhotos
from connection import *
import os 

path = 'media/example_13'

if not os.path.exists(path):
    os.mkdir(path)

client = TelegramClient('tg_session', api_id, api_hash)
client.start()
messages = client.iter_messages(group, filter=InputMessagesFilterPhotos)
for message in messages:
    client.download_media(message, path)

files = os.listdir(path)
result = 0
for file in files:
    result += os.stat(f'{path}/{file}').st_size
print(result)


