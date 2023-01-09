import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get(url='https://parsinger.ru/html/index1_page_1.html') as resp:
            print((await resp.text())[:100])


asyncio.run(main())