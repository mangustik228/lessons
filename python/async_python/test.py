import asyncio
import random


async def foo(i):
    print(f'start task {i}')
    val = random.uniform(0.5, 3)
    await asyncio.sleep(val)
    print(f'finish task {i}')
    return val


async def main():
    tasks = [asyncio.create_task(foo(i), name=f"task_{i}") for i in range(10)]
    print('All tasks created')
    while len(tasks):
        done, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        for task in done:
            print(f'task completed {task.get_name()},'
                  f'flag - {task.done()},'
                  f'result - {task.result()}')


if __name__ == '__main__':
    asyncio.run(main())
