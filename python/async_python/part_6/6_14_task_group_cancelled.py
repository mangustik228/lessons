import asyncio


async def coro(n):
    task_name = asyncio.current_task().get_name()
    print(f'{task_name}: start')
    await asyncio.sleep(n)
    print(f'{task_name}: finished')


async def main():
    async with asyncio.TaskGroup() as group:
        tasks = [group.create_task(
            coro(i), name=f"TASK_{i:02}") for i in range(1, 4)]
        await asyncio.sleep(0.5)
        tasks[0].cancel()
    for task in tasks:
        name = task.get_name()
        print(f"{name}: done={task.done()}, cancelled={task.cancelled()}")

if __name__ == '__main__':
    asyncio.run(main())
