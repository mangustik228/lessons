import asyncio

from loguru import logger


async def foo(n: int, semaphore: asyncio.Semaphore):
    async with semaphore:
        await asyncio.sleep(1)
        logger.debug(f'{n} is done!')


async def main():
    semaphore = asyncio.Semaphore(3)  # Например, ограничим до 10 корутин
    tasks = []

    for i in range(10):
        task = asyncio.create_task(foo(i, semaphore))
        tasks.append(task)

    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
