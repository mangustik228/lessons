import asyncio


async def my_coroutine(seconds):
    await asyncio.sleep(1)


async def main():
    task = asyncio.create_task(my_coroutine(3))
    await asyncio.sleep(0.2)
    task.cancel()
    asyncio.cancelling
    print(task.canсelling())

asyncio.run(main())
