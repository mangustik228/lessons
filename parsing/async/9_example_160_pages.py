import aiohttp
import asyncio
from parsel import Selector
import os
import json
from time import perf_counter

PATH = 'data.json'

links = [f'https://parsinger.ru/html/index{index}_page_{pagen}.html' for index in range(1, 5) for pagen in range(1, 5)]
category = ['watch', 'mobile', 'mouse', 'hdd', 'headphones']
urls = [f'https://parsinger.ru/html/{cat}/{i}/{i}_{x}.html' for cat, i in zip(category, range(1, len(category) + 1)) for x in range(1, 33)]



def parse_page(sel: Selector):
    result = {}
    result['title'] = sel.xpath('//p[@id="p_header"]/text()').get()
    result['price'] = sel.xpath('//span[@id="price"]/text()').get()
    result['old_price'] = sel.xpath('//span[@id="old_price"]/text()').get()
    result['in_stock'] = sel.xpath('//span[@id="in_stock"]/text()').get()
    result['article'] = sel.xpath('//p[@class="article"]/text()').get()
    description = {}
    for li in sel.xpath('//li'):
        description[li.xpath('./@id').get()] = ''.join(li.xpath('./text()').get().split(':')[1:])
    result['description'] = description
    return result

def write_string(result:dict):
    if not os.path.exists(PATH):
        with open(PATH, 'w', encoding='utf-8') as file:
            json.dump([result], file, indent=4, ensure_ascii=False)
    else:
        with open(PATH, 'r', encoding='utf-8') as file:
            data:list = json.load(file)
        data.append(result)
        with open(PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


async def main(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            sel = Selector(await resp.text())
            result = parse_page(sel)
            write_string(result)


if __name__ == '__main__':
    start = perf_counter()
    task = [main(link) for link in urls]
    asyncio.run(asyncio.wait(task))
    end = perf_counter()
    print(f'Время работы скрипта: {end - start}')