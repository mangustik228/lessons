import requests
import json

url = 'https://parsinger.ru/downloads/get_json/res.json'
response = requests.get(url)
response.encoding = 'utf-8'
data = json.loads(response.text)
info = {}
for item in data:
    if info.get(item.get('categories')):
        info[item.get('categories')] += int(item.get('count'))
    else:
        info[item.get('categories')] = int(item.get('count'))
print(info)