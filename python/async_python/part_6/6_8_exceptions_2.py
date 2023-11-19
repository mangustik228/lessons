import asyncio


# Определение асинхронной функции, которая имитирует ошибку
async def failing_coroutine():
    # Асинхронное ожидание на 1 секунду
    await asyncio.sleep(1)
    # Генерируем исключение ValueError
    raise ValueError("Возникла ошибка в корутине failing_coroutine()")


# Определение асинхронной функции, которая успешно завершает свою работу
async def successful_coroutine():
    # Асинхронное ожидание на 1 секунду
    await asyncio.sleep(2)
    # Вывод сообщения об успешном выполнении
    print("Успешное выполнение")


# Определение основной асинхронной функции
async def main():
    tasks: list[asyncio.Task] = [asyncio.create_task(failing_coroutine()), asyncio.create_task(
        successful_coroutine())]  # Создание списка задач (корутин) для выполнения
    # Обработка исключений, возникающих во время выполнения корутин
    print(len(asyncio.all_tasks()))
    try:
        # Запуск всех задач одновременно
        await asyncio.gather(*tasks)
    # Ловим исключение ValueError, если возникло
    except ValueError as _ex:
        # Выводим информацию об исключении
        print(_ex)

    print(len(asyncio.all_tasks()))
    # Перебираем все задачи и выводим результат их выполнения
    for i, task in enumerate(tasks, start=1):
        # Получаем исключение из задачи, если оно возникло
        if not task.done():
            await task
        exc = task.exception()

        # Если исключение возникло
        if exc:
            # Выводим информацию об исключении
            print(f"Задача {i}: Исключение - {exc}")
        else:
            # В противном случае сообщаем об успешном выполнении
            print(f"Задача {i}: Успешно выполнена")


# Запуск асинхронной функции main()
asyncio.run(main())
