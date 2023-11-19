import asyncio


async def main():
    lifo_queue = asyncio.LifoQueue()
    await lifo_queue.put(None)
    await lifo_queue.put("first")
    await lifo_queue.put("second")
    await lifo_queue.put("third")
    await lifo_queue.put("fourth")

    print(f"{lifo_queue.qsize() = }")
    while True:
        lifo_queue.task_done()
        item = await lifo_queue.get()
        if item is None:
            break
        # print(lifo_queue)
        print(f'item got from lifo-queue: {item}')


if __name__ == '__main__':
    asyncio.run(main())
