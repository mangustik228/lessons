from telethon import TelegramClient, sync, connection, events
from telethon.tl.functions.users import GetFullUserRequest
from connection import api_hash, api_id

lst = [5125814085, 5423813689, 5395359919, 5330282124, 5451738743, 5319101536,
       5599808192, 5552200609, 5560704798, 5421516684, 5596049016, 5313438049,
       5530400713, 5595171770, 5373895551, 5582701295, 5401839698, 5443556002,
       5445202221, 5394891665, 5486227453, 5342098799, 5486370067, 5576022537,
       5539803054, 5523594628, 5449816597, 5235694206]

client = TelegramClient('tg_session', api_id, api_hash)
client.start()
users = client.iter_participants('t.me/Parsinger_Telethon_Test')

result = 0

for user in users:
    user_full_about = client(GetFullUserRequest(user))
    try:
        value = int(user_full_about.full_user.about)
    except TypeError:
        value = None
    if value in lst:
        result += value
print(result)    

