import asyncio


lock_1 = asyncio.Lock()
lock_2 = asyncio.Lock()


async def task(i: int, lock_1: asyncio.Lock, lock_2: asyncio.Lock):
    print(f'Задача {i} блокирует 1...')
    async with lock_1:
        print(f'Задача {i} блокирует 2...')
        await asyncio.sleep(0.2)
        async with lock_2:
            print("never awaited")


async def main():
    await asyncio.gather(task(1, lock_1, lock_2), task(2, lock_2, lock_1))


if __name__ == '__main__':
    asyncio.run(main())
