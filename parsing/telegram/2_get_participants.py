from telethon import TelegramClient, events, sync, connection
from connection import api_hash, api_id

client = TelegramClient('get_participants', api_id, api_hash)

client.start()
participants = client.get_participants('t.me/Parsinger_Telethon_Test')
# print(participants)
data = []
for participant in participants:
    data.append(f'{participant.first_name} {participant.last_name}')
print(data)
