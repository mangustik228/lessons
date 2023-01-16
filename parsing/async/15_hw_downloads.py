import os 
from parsel import Selector 
import asyncio 
import aiofiles
import aiohttp
import requests
from loguru import logger

URL = 'https://parsinger.ru/asyncio/aiofile/3'
DOWNLOADED_IMAGES = set()
FOLDER = 'media'
logger.add('15_logs.log')

class Parser:
    def __init__(self):
        self.check_folder()
    
    @staticmethod
    def check_folder():
        if not os.path.exists(FOLDER):
            os.mkdir(FOLDER)
            logger.info(f'Создал папку: {FOLDER}')

    def finish_spider(self):
        logger.info(f'Закончил парсить. самоликвидируюсь')
        path = f'{os.getcwd()}/{FOLDER}'
        files = os.listdir(path)
        result = 0
        for file in files:
            result += os.stat(f'{path}/{file}').st_size
        logger.info(f'Повторных изображений: {len(DOWNLOADED_IMAGES)}')
        logger.info(f'Скачено {len(files)} файлов. Общее кол-во байт: {result}')
        del self


    def get_first_links(self):
        resp = requests.get(f'{URL}/index.html')
        resp.encoding = 'utf-8'
        sel = Selector(resp.text)
        self.links = []
        for link in sel.xpath('//a/@href'):
            self.links.append(f'{URL}/{link.get()}')
        logger.info(f'Спарсил {len(self.links)} ссылок')
        
    async def init_async_parsing(self):
        logger.info('Запущен асинхронный парсер')
        async with aiohttp.ClientSession() as self.session:
            tasks = []
            for link in self.links:
                task = asyncio.create_task(self.first_depth(link))
                tasks.append(task)
            logger.info(f'Создал {len(tasks)} при инициализации event loop')
            logger.info(self.links)
            await asyncio.gather(*tasks)


    async def first_depth(self, url:str):
        async with self.session.get(url) as resp:
            logger.info(f'{resp.url = }')
            sel = Selector(await resp.text())
            base_url = '/'.join(url.split('/')[:-1])
            tasks = []
            for link in sel.xpath('//a/@href'):
                new_url = f'{base_url}/{link.get()}'
                logger.info(f'{new_url = }')
                task = asyncio.create_task(self.second_depth(new_url))
                tasks.append(task)
            await asyncio.gather(*tasks)

    async def second_depth(self, url):
        async with self.session.get(url) as resp:
            sel = Selector(await resp.text())
            images = sel.xpath('//img/@src')
            tasks = []
            for image in images:
                link:str = image.get()
                file_name = link.split('/')[-1]
                task = asyncio.create_task(self.get_photo(link, file_name))
                tasks.append(task)
            await asyncio.gather(*tasks)

    @staticmethod
    def get_path_file(file_name):
        return f'{FOLDER}/{file_name}'

    async def get_photo(self, url, file_name):
        if url in DOWNLOADED_IMAGES:
            return
        DOWNLOADED_IMAGES.add(url)
        async with self.session.get(url) as resp:
            path = self.get_path_file(file_name)
            async with aiofiles.open(path, 'wb') as file:
                async for part in resp.content.iter_chunked(1024):
                    await file.write(part)



parser = Parser()
parser.get_first_links()
asyncio.run(parser.init_async_parsing())
parser.finish_spider()