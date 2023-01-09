from telethon import TelegramClient, events, sync, connection
from connection import api_hash, api_id

client = TelegramClient('session_name', api_id=api_id, api_hash=api_hash)
client.start()
print(client.get_me())
client.disconnect()