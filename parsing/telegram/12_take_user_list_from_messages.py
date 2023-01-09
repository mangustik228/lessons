from telethon import TelegramClient, sync, events, connection
from connection import *
import re


client = TelegramClient('tg_session', api_id, api_hash)
client.start()
messages = client.iter_messages(group)
users_lst = []
for message in messages:
    try: 
        int(message.message)
        users_lst.append(message.from_id.user_id)
    except (TypeError, ValueError):
        pass
print(users_lst)