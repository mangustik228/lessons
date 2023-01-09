from telethon import TelegramClient, sync, connection, events
from connection import * 

client = TelegramClient('tg_session', api_id, api_hash)
client.start()
user = client.get_entity(5330282124)
messages = client.iter_messages(group, from_user=user)
result = 0
for message in messages:
    try: 
        value = int(message.message)
        result += value
    except (TypeError, ValueError):
        pass
    print(message.message)
print(f'{result = }')