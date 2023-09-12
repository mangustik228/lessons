import asyncio
from time import sleep


async def delay(n):
    await asyncio.sleep(n)
    print("done")


async def foo():
    await asyncio.sleep(0.0001)


async def main():
    task = asyncio.create_task(delay(2))
    count = 0
    print('start task')
    while not task.done():
        await foo()
        count += 1
    print(count)

if __name__ == '__main__':

    asyncio.run(main())
