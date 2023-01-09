import aiohttp
import asyncio

url = 'http://httpbin.org/ip'
proxy = '176.56.35.113:3891'
login = 'user90481'
passwd = 'mgbsi2'
cur_proxy = f'http://{login}:{passwd}@{proxy}'


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, proxy=cur_proxy) as resp:
            print(await resp.text())

if __name__ == '__main__':
    asyncio.run(main())