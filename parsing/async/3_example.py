import asyncio

async def my_sleep():
    loop = asyncio.get_running_loop()
    loop.create_task()
    await asyncio.sleep(3)
    print('hello world')

asyncio.run(my_sleep())