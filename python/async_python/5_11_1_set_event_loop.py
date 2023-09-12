

import asyncio


async def task_1(idx):
    print(f"Task 1 {idx} is running")
    await asyncio.sleep(1)
    print(f"Task 1 {idx} is complete")


async def task_2(idx):
    print(f"Task 2 {idx} is running")
    await asyncio.sleep(1)
    print(f"Task 2 {idx} is complete")


async def main_1():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    tasks = [asyncio.ensure_future(task_1(i)) for i in range(3)]
    await asyncio.gather(*tasks)
    loop.close()


async def main_2():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    tasks = [asyncio.ensure_future(task_2(i)) for i in range(3)]
    await asyncio.gather(*tasks)
    loop.close()


asyncio.run(main_1())
asyncio.run(main_2())
