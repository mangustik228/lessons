import asyncio


event = asyncio.Event()


async def waiter():
    await event.wait()
    print('event done!')


async def setter():
    await asyncio.sleep(1)
    event.set()


async def main():
    await asyncio.gather(waiter(), setter())


if __name__ == '__main__':
    asyncio.run(main())
