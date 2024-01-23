import asyncio


async def file_reader(filename: str) -> str:
    """Корутина для чтения файла"""
    await asyncio.sleep(1)
    with open(filename) as f:
        data: str = f.read()
    return data


async def get_data(data: int) -> dict:
    """Корутина, для возврата переданного числа в виде словаря вида {'data': data}"""
    if data == 0:
        raise Exception('Нет данных...')
    return {'data': data}


# Базовая корутина
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(get_data(1))
        task2 = tg.create_task(get_data(2))
        task3 = tg.create_task(file_reader('fake.png'))
        task4 = tg.create_task(get_data(0))
    result = [task1.result(), task2.result(), task3.result(), task4.result()]
    print('Готово!!!', result)


asyncio.run(main())
