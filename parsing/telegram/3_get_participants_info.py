from telethon import TelegramClient, events, sync, connection
from connection import api_hash, api_id

client = TelegramClient('tg_session', api_id, api_hash)

client.start()
participants = client.get_participants('t.me/Parsinger_Telethon_Test')
data = []
for participant in participants:
    value = f'{participant.id} {participant.first_name} {participant.last_name} {participant.phone}'
    data.append(value)
print(data)