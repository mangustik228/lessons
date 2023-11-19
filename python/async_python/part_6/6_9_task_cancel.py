import asyncio


async def my_task(n):
    print(f"start task {asyncio.current_task().get_name()}")
    await asyncio.sleep(n)
    print(f"finish task {asyncio.current_task().get_name()}")


async def main():
    tasks = [asyncio.create_task(
        my_task(n), name=f"MY-TASK-{n}") for n in range(5)]
    await asyncio.sleep(2)
    for task in tasks:
        if not task.done():
            task.cancel()
            print(f"{task.get_name()} canceled")
        print(f'{task.get_name()} cancelled: {task.cancelled()}')
        print(task)
        await asyncio.sleep(0)
        print(f'{task.get_name()} cancelled: {task.cancelled()}')
        print(task)
        print("\n\n")
        # await asyncio.sleep(0) Если стоит тут, то будет False... т.к. нет переключение контекста


if __name__ == '__main__':
    asyncio.run(main())
