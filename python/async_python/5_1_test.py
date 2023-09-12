import asyncio

from loguru import logger


async def main(n):
    await asyncio.sleep(1)
    logger.debug(f'Привет из цикла {n}')


if __name__ == '__main__':
    asyncio.run(main(0), debug=True)
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main(1))
    logger.debug(f'Закончил цикл 1')
    del loop

    loop = asyncio.new_event_loop()
    loop.run_until_complete(main(2))
    logger.debug(f'Закончил цикл 2')
