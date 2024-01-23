import asyncio

condition = asyncio.Condition()


async def consumer(condition: asyncio.Condition):
    async with condition:
        print('starting to wait condition...')
        await condition.wait()
        print(f"condition is True")


async def producer(condition: asyncio.Condition):
    await asyncio.sleep(1)
    async with condition:
        condition.notify_all()


async def main():
    await asyncio.gather(consumer(condition), producer(condition))


if __name__ == '__main__':
    asyncio.run(main())
