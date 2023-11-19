import asyncio


async def foo():
    await asyncio.sleep(1)
    for stack in asyncio.current_task().get_stack():
        print(stack)


async def main():
    await asyncio.gather(foo(), foo())

asyncio.run(main())
