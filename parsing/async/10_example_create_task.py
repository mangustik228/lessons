import requests, json, os 
from parsel import Selector 
import asyncio 
import aiohttp

BASE_URL = 'https://parsinger.ru/html/'
START_URL = 'https://parsinger.ru/html/index1_page_1.html'
PATH = 'async_data.json'

def get_selector(url):
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    return Selector(resp.text)

class Parser:
    def __init__(self) -> None:
        self.lst_categories = []
        self.lst_paginations = []
        self.data = []

    def get_categories(self):
        sel = get_selector(START_URL)
        links = sel.xpath('//div[@class="nav_menu"]/a/@href')
        for link in links:
            self.lst_categories.append(BASE_URL + link.get())
        print(f'Get categories {len(self.lst_categories)}')
        return self

    def get_paginations(self):
        for url in self.lst_categories:
            sel = get_selector(url)
            links = sel.xpath('(//div[@class="pagen"])[1]/a/@href')
            for link in links:
                self.lst_paginations.append(BASE_URL + link.get())
        print(f'Get paginations {len(self.lst_paginations)}')



    def finish_parsing(self):
        print(f'Parsed products {len(self.data)}')
        with open(PATH, 'w') as file:
            json.dump(self.data, file)

    def extract_product_links(self, response):
        sel = Selector(response)
        links = sel.xpath('//a[@class="name_item"]/@href')
        pages_for_tasks = []
        for link in links:
            pages_for_tasks.append(BASE_URL + link.get())
        return pages_for_tasks
    

    async def pars_page(self, session: aiohttp.ClientSession, url):
        async with session.get(url) as resp:
            sel = Selector(await resp.text())
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
            self.data.append(result)    


    async def get_product_links(self, session: aiohttp.ClientSession, url):
        async with session.get(url) as resp:
            response = await resp.text()
        urls = self.extract_product_links(response)
        tasks = []
        for url in urls:
            task = asyncio.create_task(self.pars_page(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks)


    async def start(self):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for url in self.lst_paginations:
                task = asyncio.create_task(self.get_product_links(session, url))
                tasks.append(task)
            await asyncio.gather(*tasks)


if __name__ == '__main__':
    parser = Parser()
    parser.get_categories().get_paginations()
    asyncio.run(parser.start())
    parser.finish_parsing()