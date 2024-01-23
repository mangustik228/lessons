import asyncio


event = asyncio.Event()
# event.set()  # Устанавливает флаг в True
# event.clear()  # Устанавливает флаг в False
# event.wait()  # Блокирует задачу пока не будет True (Используем осторожно)
# event.is_set()  # Проверить состояние флага


async def wait_event():
    print(f'start to wait')
    await event.wait()
    print(f'event happened')


async def my_event():
    print("something doing")
    await asyncio.sleep(0.1)
    event.set()
    await asyncio.sleep(0.1)
    print("I'm did it")


async def main():
    async with asyncio.TaskGroup() as group:
        group.create_task(my_event())
        group.create_task(wait_event())


if __name__ == '__main__':
    asyncio.run(main())
