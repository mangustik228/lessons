from time import sleep
from random import randint
import asyncio


async def world():
    await asyncio.sleep(1)
    print('world!', end=" ")

async def hello():
    print('hello', end=" ")

async def end():
    await asyncio.sleep(2)
    print('end...')


async def main():
    await asyncio.gather(end(), hello(), world())


# async def main():
    # end_var = asyncio.create_task(end())
    # world_var = asyncio.create_task(world())
    # hello_var = asyncio.create_task(hello())
    # await end_var
    # await world_var
    # await hello_var

asyncio.run(main())