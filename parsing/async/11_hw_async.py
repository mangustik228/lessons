import aiohttp
import asyncio
import requests
from parsel import Selector
import re
from loguru import logger


logger.add(
    sink='log.log',
)

BASE_URL = 'https://parsinger.ru/html/'
START_URL = 'https://parsinger.ru/html/index1_page_1.html'

class Parser:
    def __init__(self):
        self.pagen = []
        self.urls_categories = []
        self.urls_pagination = []
        self.data = []

    @staticmethod
    def full_url(url):
        return BASE_URL + url

    @staticmethod
    def get_selector(url):
        resp = requests.get(url)
        resp.encoding = 'utf-8'
        return Selector(resp.text)

    def get_categories(self, start_url):
        logger.debug(f'Начинаю собирать ссылки')
        sel = self.get_selector(start_url)
        for link in sel.xpath('//div[@class="nav_menu"]/a/@href'):
            self.urls_categories.append(self.full_url(link.get()))
        logger.debug(f'Собрал {len(self.urls_categories)} ссылок')

    def get_pagination(self):
        logger.debug('Собираю пагинации')
        for url in self.urls_categories:
            sel = self.get_selector(url)
            for link in sel.xpath('//div[@class="pagen"][1]/a/@href'):
                self.urls_pagination.append(self.full_url(link.get()))
        logger.debug(f'Собрал {len(self.urls_pagination)} ссылок')

    def print_result(self):
        logger.info(f'{sum(self.data)}')

    async def get_value(self, url, session: aiohttp.ClientSession):
        async with session.get(url) as resp:
            sel = Selector(await resp.text())
            price = sel.xpath('//span[@id="price"]/text()').get()
            old_price = sel.xpath('//span[@id="old_price"]/text()').get()
            in_stock = sel.xpath('//span[@id="in_stock"]/text()').get()
            price = int(re.sub(r'\D', '', price))
            old_price = int(re.sub(r'\D', '', old_price))
            in_stock = int(re.sub(r'\D', '', in_stock))
            result = (price - old_price) * in_stock
            self.data.append(result)

    async def get_links(self, url, session: aiohttp.ClientSession):
        logger.debug('В асинхронной части, собираю ссылки')
        async with session.get(url) as resp:
            response = await resp.text()
        sel = Selector(response)
        tasks = []
        for link in sel.xpath('//a[@class="name_item"]/@href'):
            task = asyncio.create_task(self.get_value(self.full_url(link.get()), session))
            tasks.append(task)
        await asyncio.gather(*tasks)


    async def start_parsing(self):
        logger.debug('Запускаю парсер')
        async with aiohttp.ClientSession() as session:
            tasks = []
            for url in self.urls_pagination:
                task = asyncio.create_task(self.get_links(url, session))
                tasks.append(task)
            await asyncio.gather(*tasks)





if __name__ == '__main__':
    parser = Parser()
    parser.get_categories(START_URL)
    parser.get_pagination()
    asyncio.run(parser.start_parsing())
    parser.print_result()