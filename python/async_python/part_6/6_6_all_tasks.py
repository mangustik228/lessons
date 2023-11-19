import asyncio


async def my_task(i: int):
    print(f'start task: {i}')
    await asyncio.sleep(3)
    print(f'end task: {i}')

# DEADLOCK


async def main():
    [asyncio.create_task(my_task(i)) for i in range(5)]
    await asyncio.all_tasks(asyncio.gather())


if __name__ == '__main__':
    asyncio.run(main())
