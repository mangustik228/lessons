import aiohttp
import asyncio
import aiofiles
from asyncio.exceptions import TimeoutError

url = 'http://httpbin.org/ip'
async def main():
    async with aiofiles.open('proxy_list.txt', mode='r') as file:
        for prx in await file.readlines():
            proxy = f'http://{prx.strip()}'
            try: 
                async with aiohttp.ClientSession() as session:
                    async with session.get(url=url, proxy=proxy, timeout=1) as resp:
                        if resp.ok:
                            print(f'good proxy, {resp.status = }, {prx.strip() = }')
                        else:
                            print(f'bad proxy, {resp.status = }, {prx.strip() = }')
            except TimeoutError: 
                continue
            except Exception as e:
                print(e)


if __name__ == '__main__':
    asyncio.run(main())