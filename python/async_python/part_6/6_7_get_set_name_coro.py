import asyncio


async def my_task():
    print(f"name coro before the change: {asyncio.current_task().get_name()}")
    asyncio.current_task().set_name("new name")
    print(f"name coro after the change: {asyncio.current_task().get_name()}")


async def main():
    task = asyncio.create_task(my_task())
    await asyncio.sleep(0.2)
    task.set_name("new_name")
    await task

if __name__ == '__main__':
    asyncio.run(main())
