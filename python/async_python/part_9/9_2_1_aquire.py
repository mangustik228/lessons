import asyncio

lock = asyncio.Lock()


async def delay_context(n):
    async with lock:
        print(f"coro_with_manager {n} locked")
        await asyncio.sleep(1)
        print(f'coro_with_manager {n} finished')


async def delay(n):
    '''first version with lock.aquire() and lock.release()'''
    try:
        await lock.acquire()
        print(f'coro {n} started')
        print(f"coro {n} locked")
        await asyncio.sleep(1)
    finally:
        lock.release()
    print(f"coro {n} unlocked")
    print(f'coro {n} finished')


async def main():
    async with asyncio.TaskGroup() as group:
        group.create_task(delay(1))
        group.create_task(delay(2))

    async with asyncio.TaskGroup() as group:
        group.create_task(delay_context(1))
        group.create_task(delay_context(2))


if __name__ == '__main__':
    asyncio.run(main())
