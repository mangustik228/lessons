from telethon import TelegramClient, sync, events, connection
from telethon.tl.types import InputMessagesFilterPinned
from connection import *

client = TelegramClient('tg_session', api_id, api_hash)
client.start()
message = client.get_messages(group, filter=InputMessagesFilterPinned)
print(message[0].from_id.user_id)