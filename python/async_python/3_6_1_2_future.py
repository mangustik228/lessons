import asyncio


async def do_some_work_1(x):              # Определяем первую асинхронную функцию
    print(f"Doing some work 1: {x}")      # Выводим сообщение о том, что началась выполнение первой функции
    await asyncio.sleep(x)                # Останавливаем выполнение функции на время x секунд
    return x * 2                          # Возвращаем результат выполнения функции


async def do_some_work_2(x):              # Определяем вторую асинхронную функцию
    print(f"Doing some work 2: {x}")      # Выводим сообщение о том, что началась выполнение второй функции
    await asyncio.sleep(x)                # Останавливаем выполнение функции на время x секунд
    return x + 2                          # Возвращаем результат выполнения функции


async def main():                                               # Определяем главную асинхронную функцию
    future_1 = asyncio.ensure_future(do_some_work_1(2))         # Создаем объект Future для первой задачи
    result_1 = await future_1                                   # Ждем результата работы 1 (повторно)
    future_2 = asyncio.ensure_future(do_some_work_2(result_1))  # Создаем будущее, которое содержит результат работы 2
    result_2 = await future_2                                   # Ждем результата работы 2
    print(f"Result future_1: {result_1}")                       # Выводим результат работы 1
    print(f"Result future_2: {result_2}")                       # Выводим результат работы 2


asyncio.run(main()) 