import time 
import aiofiles
import os 
import aiohttp
import asyncio
from parsel import Selector 
from loguru import logger

URL = 'https://parsinger.ru/asyncio/aiofile/2'
FOLDER = 'media'
DOWNLOADED_IMAGE = set()
logger.add('14_hw_logs.log')



async def get_photo(url, file_name, session):
    if url in DOWNLOADED_IMAGE:
        logger.debug(f'{url} - Уже парсился, делаем return')
        return
    DOWNLOADED_IMAGE.add(url)
    async with session.get(url) as response:
        async with aiofiles.open(f'{FOLDER}/{file_name}', mode='wb') as file:
            async for part in response.content.iter_chunked(1024):
                await file.write(part)
            logger.debug(f'{file_name} - Скачено')


async def pars_page(session: aiohttp.ClientSession, url:str):
    async with session.get(url) as resp:
        sel = Selector(await resp.text())
        logger.debug(f'Ответ получен со страницы {url}.  status:{resp.status}')
        tasks = []
        for image in sel.xpath('//img/@src'):
            src = image.get()
            file_name = src.split('/')[-1]
            task = asyncio.create_task(get_photo(src, file_name, session))
            tasks.append(task)
        await asyncio.gather(*tasks)


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{URL}/index.html') as resp:
            sel = Selector(await resp.text())
            tasks = []
            links = sel.xpath('//a/@href')
            logger.debug(f'Первую страницу успешно спарсил, получил {len(links)} Ссылок')
            for link in links:
                url = f'{URL}/{link.get()}'
                task = asyncio.create_task(pars_page(session, url))
                tasks.append(task)
            await asyncio.gather(*tasks)

if not os.path.exists(FOLDER):
    os.mkdir(FOLDER)
    logger.debug(f'{FOLDER} - папка создана')

logger.debug(f'Запускаем event-loop')
asyncio.run(main())

result = []
files = os.listdir(f'{os.getcwd()}/{FOLDER}')
for file in files:
    path = f'{os.getcwd()}/{FOLDER}/{file}'
    result.append(os.stat(path).st_size)
logger.info(f'Скачено файлов: {len(files)}, Общий объем: {sum(result)} байт')