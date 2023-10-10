import asyncio
import random

from loguru import logger


async def foo():
    if random.randint(0, 10) < 5:
        return "done!"
    else:
        raise ValueError("must be more 5")


async def main():
    result = await asyncio.gather(*[foo() for i in range(10)], return_exceptions=True)
    for item in result:
        logger.debug(f'{type(item)} | {item}')
        if issubclass(item.__class__, Exception):
            logger.debug(f'error')


if __name__ == '__main__':
    asyncio.run(main())
