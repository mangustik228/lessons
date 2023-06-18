import httpx
import asyncio
import aiofiles


ADDRS = [
    "205.134.165.88",
    "162.159.128.64",
    "162.159.129.64",
    "39.106.180.57",
    "2606:4700:0000:0000:0000:0000:6812:5864",
    "195.34.20.229",
    "2606:4700:0007:0000:0000:0000:A29F:8040",
    "8.211.3.146",
    "185.73.195.21",
    "178.248.239.172",
    "185.73.195.103",
    "185.73.195.89",
    "185.73.195.102",
    "195.34.20.253",
    "185.73.195.91",
    "185.73.195.104",
    "185.73.195.93",
    "185.73.195.105",
    "2606:4700:0000:0000:0000:0000:6812:5964",
    "185.73.195.88",
    "195.34.20.232",
    "195.34.20.228",
    "195.34.20.233",
    "185.73.195.106",
    "211.194.115.227",
    "2606:4700:0007:0000:0000:0000:A29F:8140",
    "185.73.195.90",
    "195.34.20.252",
    "8.222.231.72",
    "104.18.88.100",
    "104.18.89.100",
    "185.146.157.33",
    "185.73.195.92",
    "93.189.42.141",
    "37.140.198.35",
    "188.225.76.48",
    "188.225.77.217",
    "195.93.181.239",
    "188.225.33.22",
    "185.146.157.216",
    "188.225.39.160",
    "5.180.180.193",
    "168.119.89.154",
    "185.47.207.187",
    "148.251.128.124",
    "78.24.222.28",
    "51.15.34.25",
    "148.251.128.123",
    "148.251.128.57",
    "148.251.128.126",
    "80.93.183.236",
    "81.200.153.25",
    "188.120.254.72"
]


HEADERS = {
    "User-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Host": "www.ozon.ru"
}


async def get_request(url):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=HEADERS, follow_redirects=True)
            response.raise_for_status()  # Проверка на успешный статус ответа (200)
            print(response.text[:100])
            print(f'Succesfull!!! {url}')
            with open('hello.html', 'w') as file:
                file.write(response.text)
        except httpx.HTTPStatusError as exc:
            print(f"HTTP error occurred: {exc}")
        except Exception as exc:
            print(f"An error occurred: {exc}")


async def main():
    tasks = []
    for addr in ADDRS:
        url = f"http://{addr}/seller/1"
        task = asyncio.create_task(get_request(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
