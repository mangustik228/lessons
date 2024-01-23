import asyncio


async def some_coro(n):
    task_name = asyncio.current_task().get_name()
    print(f'start {n} {task_name}')
    await asyncio.sleep(n)
    print(f'finish {n} {task_name}')
    return n * 2


async def main():
    async with asyncio.TaskGroup() as group:
        tasks = [group.create_task(
            some_coro(i), name=f'MyTask_{i:02}') for i in range(5)]
    for task in tasks:
        print(f"{task.get_name()}: {task.result()}")

    print("success")

if __name__ == '__main__':
    asyncio.run(main())
