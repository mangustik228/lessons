import asyncio


async def my_coroutine():
    print("Корутина начала выполнение")
    await asyncio.sleep(3)
    print("Корутина завершена")


async def main():
    task = asyncio.shield(my_coroutine())
    await task

asyncio.run(main())
