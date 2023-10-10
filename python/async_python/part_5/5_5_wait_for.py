import asyncio

from loguru import logger


async def foo():
    await asyncio.sleep(0.2)


async def main():
    try:
        await asyncio.wait_for(foo(), timeout=0.1)
    except asyncio.TimeoutError as e:
        logger.error(f'{foo} TIMEOUT ERROR')

if __name__ == '__main__':
    asyncio.run(main())
