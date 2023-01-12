from loguru import logger 
from parsel import Selector 
import aiohttp
import asyncio
import requests


start_url = 'https://parsinger.ru/asyncio/create_soup/1/index.html'
base_url = 'https://parsinger.ru/asyncio/create_soup/1/'
result = 0

async def inspect_page(url, session: aiohttp.ClientSession):
    global result
    async with session.get(url) as resp:
        if resp.status == 200:
            sel = Selector(await resp.text())
            res = sel.xpath('//p/text()').get()
            result += int(res)
            

async def get_value(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(inspect_page(url, session))
            tasks.append(task)
        await asyncio.gather(*tasks)

resp = requests.get(start_url)
sel = Selector(resp.text)
urls = []
for link in sel.xpath('//a/@href'):
    urls.append(base_url + link.get())

asyncio.run(get_value(urls))
logger.info(result)