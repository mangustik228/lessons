import asyncio

# Объявление корутины consumer

condition = asyncio.Condition()


async def consumer(name):
    async with condition:
        print(f"{name} start")
        await condition.wait()
        print(f'{name} - done!')


async def producer():
    for i in range(1, 6):
        async with condition:
            print(f"{i} - notified")
            condition.notify()
        await asyncio.sleep(1)


async def main():
    consumers = [asyncio.create_task(
        consumer(f'Потребитель {i}')) for i in range(1, 6)]

    await asyncio.gather(*consumers, producer())

asyncio.run(main())
