import aiohttp
import asyncio

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
url = 'http://httpbin.org/get'
data = {'sessionKey': 'hello world', 'format': 'json', 'platformId': 1, 'my_new_variable': 'new_variable'}

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=data, timeout=2) as resp:
            # По истечанию timeout выловим asyncio.exceptions.TimeoutError
            print(await resp.text())


asyncio.run(main())