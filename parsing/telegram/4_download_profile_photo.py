from telethon import TelegramClient, sync, events, connection
from connection import api_hash, api_id
import os

client = TelegramClient('tg_session', api_id, api_hash)
path = 'media/tg_avatars'


client.start()
participants = client.get_participants('t.me/Parsinger_Telethon_Test')
for index, participant in enumerate(participants):
    client.download_profile_photo(participant, f'{path}/{participant.id}.jpg', download_big=True)



files = os.listdir(path)
result = 0
for file in files:
    result += os.stat(f'{path}/{file}').st_size
print(f'Скаченные файлы занимают: {result} байт')
