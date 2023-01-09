from parsel import Selector
import requests

resp = requests.get('https://parsinger.ru/table/5/index.html')
selector = Selector(resp.text)
columns = selector.xpath('//th/text()')
mdict = {}
for i, column in enumerate(columns):
    values = selector.xpath(f'//tr/td[{i + 1}]/text()')
    data = []
    for value in values:
        data.append(float(value.get()))
    mdict[column.get()] = round(sum(data), 3)
print(mdict)