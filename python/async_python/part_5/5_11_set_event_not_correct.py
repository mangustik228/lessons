import asyncio

# Не рабочий пример


async def write_current_loop(i):
    loop = asyncio.get_event_loop()
    print(f"TASK_{i} current loop: {id(loop)}")


async def my_task(i):
    await asyncio.sleep(1)
    await write_current_loop(1)


async def main():
    await write_current_loop(0)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    await asyncio.gather(*[my_task(i) for i in range(1, 6)])


loop = asyncio.new_event_loop()
loop.run_until_complete(main())
