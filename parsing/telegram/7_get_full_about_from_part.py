from telethon import TelegramClient, sync, events, connection
from telethon.tl.functions.users import GetFullUserRequest
from connection import api_hash,api_id

lst = ['William_Price34', 'Nancy_Montgomery54', 'Gloria_Thompson4', 'Linda_Hernandez4', 'Nathan_King43',
       'Thomas_Jones56', 'Sara_Martin434', 'Elizabeth_Weber', 'Joshua_Andrews34',
       'Erica_Moore34', 'Nancy_Johnson3', 'Mildred_James', 'Brian_Johnson2',
       'James_Washington3', 'Richard_Welch', 'Scott_Stevenson32', 'Mark_Mendez980', 'Lisa_Hawkins']

client = TelegramClient('tg_session', api_id, api_hash)
client.start()

result = 0
for participant in lst:
    info = client(GetFullUserRequest(participant))
    value = int(info.full_user.about)
    result += value 
print(result)