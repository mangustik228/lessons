import aiohttp
import asyncio 

url = 'http://httpbin.org/ip'
proxy = 'http://176.56.35.113:3891'



async def main():
    async with aiohttp.ClientSession() as session:
        proxy_auth = aiohttp.BasicAuth('user90481', 'mgbsi2') # login/passw
        async with session.get(url=url, proxy=proxy, proxy_auth=proxy_auth) as resp:
            print(await resp.text())


if __name__ == '__main__':
    asyncio.run(main())