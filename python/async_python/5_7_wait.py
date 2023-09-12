import asyncio
import random

from loguru import logger


async def bar():
    raise Exception("my Exception")


async def foo(n):
    await asyncio.sleep(random.randint(1, 10) / 10)
    return f"task complete {n}"


async def generate_tasks(when, errors=False):
    if errors:
        tasks = [
            asyncio.create_task(foo(1)),
            asyncio.create_task(foo(2)),
            asyncio.create_task(bar()),
            asyncio.create_task(foo(4))
        ]
    else:
        tasks = [asyncio.create_task(foo(i)) for i in range(10)]
    good, bad = await asyncio.wait(tasks, return_when=when)
    logger.debug(f"{when} | {'with' if errors else 'without'} errors")
    logger.debug(good)
    logger.debug(bad)
    logger.debug('')


async def main():
    await generate_tasks(asyncio.FIRST_COMPLETED)
    await generate_tasks(asyncio.ALL_COMPLETED)
    await generate_tasks(asyncio.ALL_COMPLETED, errors=True)
    await generate_tasks(asyncio.FIRST_COMPLETED, errors=True)
    await generate_tasks(asyncio.FIRST_EXCEPTION, errors=True)


if __name__ == '__main__':
    asyncio.run(main())
