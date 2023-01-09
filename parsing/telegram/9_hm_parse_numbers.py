from telethon import TelegramClient, sync, events, connection
# from telethon.tl.types import InputMessagesFilterContacts
from connection import *


client = TelegramClient('tg_session', api_id, api_hash)
client.start()
messages = client.iter_messages(group)
result = 0
for message in messages:
    try:
        value = int(message.message)
        result += value
    except (TypeError, ValueError):
        pass
print(result)