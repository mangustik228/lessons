import asyncio
import time

import requests


def delay(n):
    start = time.perf_counter()
    response = requests.get("https://httpbin.org/ip")
    print(response.json())
    print(f'ended. time: {time.perf_counter() - start:.2f}')


# asyncio.to_thread()


async def main():
    async with asyncio.TaskGroup() as group:
        for _ in range(5):
            coro = asyncio.to_thread(delay, 1)
            group.create_task(coro)


if __name__ == '__main__':
    asyncio.run(main())
