import asyncio

from loguru import logger


async def foo(n):
    result = n/10
    logger.debug(f'task {n}')
    await asyncio.sleep(n/10)
    return result


async def main():
    tasks = [asyncio.create_task(foo(i)) for i in range(1, 10)]
    goods, bads = await asyncio.wait(tasks)
    logger.debug(goods)
    logger.debug(bads)
    logger.debug([good.result() for good in goods])

if __name__ == '__main__':
    asyncio.run(main())
