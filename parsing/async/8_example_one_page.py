import asyncio
import aiohttp
from parsel import Selector

url = 'https://parsinger.ru/html/index1_page_1.html'

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            sel = Selector(await resp.text())
            items = sel.xpath('//div[@class="item"]')
            for item in items:
                result = {}
                result['title'] = item.xpath('.//a[@class="name_item"]/text()').get()
                result['price'] = item.xpath('.//p[@class="price"]/text()').get()
                print(result)

asyncio.run(main())