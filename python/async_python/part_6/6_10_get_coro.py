import asyncio


async def print_hello():
    current_task = asyncio.current_task()
    current_loop = current_task.get_loop()
    print("Событийный цикл:", current_loop)


async def main():
    asyncio.create_task(print_hello())


asyncio.run(main())
