from telethon import TelegramClient, events, sync, connection
from connection import api_hash, api_id, group
from telethon.tl.types import InputMessagesFilterPhotos

client = TelegramClient('tg_session', api_id, api_hash)
client.start()


# limit - Кол-во сообщений
all_messages = client.get_messages(group, limit=10)
for message in all_messages: 
    id_user = message.from_id.user_id
    print(id_user)
    print(client.get_entity(id_user).username)

new_messages = client.get_messages(group, limit=5, filter=InputMessagesFilterPhotos)
for message in new_messages: 
    client.download_media(message, 'media/example_8')