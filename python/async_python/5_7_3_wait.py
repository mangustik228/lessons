import asyncio


async def task_func():
    print("Task executed")
    return "Task result"


async def main():
    task = asyncio.create_task(task_func())                 # Создаем задачу
    # Ожидаем завершения задачи
    _, pending = await asyncio.wait([task])
    # Проверяем, что задача завершена
    assert not pending, f"{len(pending)} pending tasks"
    print("Task result:", task.result())


asyncio.run(main())
