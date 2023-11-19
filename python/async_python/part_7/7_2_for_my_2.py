

import asyncio


async def timer_generator():
    for i in range(60):
        await asyncio.sleep(1)
        yield f'program have worked: {i} sec'


async def start_timer():
    my_timer = timer_generator()
    async for time in my_timer:
        print(time, end="\r")


async def main():
    task = asyncio.create_task(start_timer())
    await asyncio.gather(task)

if __name__ == '__main__':
    asyncio.run(main())
