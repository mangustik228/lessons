import asyncio

# Пример взаимного ожидания двух корутин


async def task(other: asyncio.Task):
    print(f'wait task: {other.get_name()}')
    await other


async def main():
    task_1 = asyncio.current_task()  # Получаем текущую Task
    task_2 = asyncio.create_task(task(task_1))
    await task(task_2)
    print(f'Код который никогда не отработает, потому что ждем задачу task_1')

if __name__ == '__main__':
    asyncio.run(main())
