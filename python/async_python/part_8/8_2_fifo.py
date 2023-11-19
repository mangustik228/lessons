

import asyncio
import random


async def producer(queue: asyncio.Queue):
    print("Producer run")
    for i in range(10):
        value = random.random()
        await asyncio.sleep(value)
        await queue.put(value)
    await queue.put(None)
    print("Producer done!")


async def consumer(queue: asyncio.Queue):
    print("Consumer run")
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f">> got {item}")
    print("Consumer done!")


async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))


if __name__ == '__main__':
    asyncio.run(main())
