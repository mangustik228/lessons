import asyncio
import random


async def foo():
    print("empty task")
    await asyncio.sleep(random.randint(1, 5))
    print("finish empty task")


async def access_resource(resource: str, lock: asyncio.Lock, i: int):
    # Блокируем доступ
    async with lock:
        print(f"[{i}] Доступ получен {resource}")
        await asyncio.sleep(1)
        print(f"[{i}] Доступ завершён {resource}")


async def main():
    # создаем объект блокировки. asyncio.Lock используется для синхронизации доступа к общему ресурсу
    lock = asyncio.Lock()
    resource = "--Защищаемый ресурс--"
    empty_tasks = [foo() for i in range(5)]
    tasks = [access_resource(resource, lock, i) for i in range(5)]
    await asyncio.gather(*tasks, *empty_tasks)

asyncio.run(main())
