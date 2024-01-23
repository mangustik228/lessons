
import asyncio

event = asyncio.Event()


async def wait_number_3(id):
    print(f"branch_{id} start to wait")
    await event.wait()
    print(f'branch_{id} event happened')
    return 42


async def iteration_number(id, n: int):
    async with asyncio.TaskGroup() as group:
        task = group.create_task(wait_number_3(id))
        for i in range(n):
            print(f'branch_{id} - {n}')
            if i == 3:
                event.set()
            await asyncio.sleep(0.1)
        if not task.done():
            task.cancel()
            print(f"branch_{id} task cancel ")
        else:
            print(f"branch_{id} task result = {task.result()}")


async def main():
    async with asyncio.TaskGroup() as group:
        group.create_task(iteration_number(1, 5))
        group.create_task(iteration_number(1, 3))


if __name__ == '__main__':
    asyncio.run(main())
