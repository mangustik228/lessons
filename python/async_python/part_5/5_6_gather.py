import asyncio
import random

from loguru import logger


async def foo():
    await asyncio.sleep(0.1)
    logger.debug(f'done!')
    return random.randint(0, 9)


async def main():
    task = asyncio.create_task(foo())
    a, b = await asyncio.gather(foo(), task)
    print(f'{a = }, {b = }')

if __name__ == '__main__':
    asyncio.run(main())
