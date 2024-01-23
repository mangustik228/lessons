import asyncio


async def coro(n):
    name = asyncio.current_task().get_name()
    print(f'{name}: start')
    await asyncio.sleep(n)
    print(f'{name}: success')
    return (n + 1) * 15


async def coro_ex_1():
    raise ValueError("Ошибка значения")


async def coro_ex_2():
    raise FileNotFoundError("Не найден файл")


async def main():
    try:
        async with asyncio.TaskGroup() as group:
            tasks = [group.create_task(
                coro(i), name=f"TASK_{i:02}") for i in range(1, 4)]
            tasks.append(group.create_task(coro_ex_1(), name="TASK_value"))
            tasks.append(group.create_task(coro_ex_2(), name="TASK_file"))
        for task in tasks:
            print(f'HIDDEN RESULT')
            name = task.get_name()
            print(f'{name}: done={task.done()}, result={task.result()}')
    except* ValueError as eg:
        for error in eg.exceptions:
            print(error)
    except* FileNotFoundError as eg:
        for error in eg.exceptions:
            print(error)

if __name__ == '__main__':
    asyncio.run(main())
