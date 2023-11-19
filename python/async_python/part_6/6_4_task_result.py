import asyncio
import random


# Определение асинхронной корутины my_coroutine
async def my_coroutine(n):
    # Вывод сообщения о начале работы корутины с учетом переданного аргумента n
    print(f"Корутина {n} запустилась")
    # Генерация случайного числа от 1 до 10 и сохранение его в переменную sleep_time
    sleep_time = random.randint(1, 10)
    # Приостановка выполнения корутины на sleep_time секунд
    await asyncio.sleep(sleep_time)
    # Вывод сообщения о завершении работы корутины с указанием времени приостановки
    print(f"Корутина {n} завершилась после {sleep_time} секунд")
    # Возвращение значения sleep_time в качестве результата выполнения корутины
    return sleep_time

# Определение основной асинхронной функции main


async def main():
    # Создание списка задач с корутинами my_coroutine с разными аргументами
    tasks = [asyncio.create_task(my_coroutine(i)) for i in range(5)]
    # Приостановка выполнения основной функции на 1 секунду
    await asyncio.sleep(1)
    # Вывод сообщения о продолжении выполнения функции main
    print("Функция main продолжает работу")
    # Создание списка таймаутов с случайными числами от 1 до 5
    timeout_list = [random.randint(1, 3) for _ in range(5)]
    # Цикл по всем задачам из списка tasks
    for i, task in enumerate(tasks):
        try:
            # Ожидание завершения задачи task с соответствующим таймаутом из списка timeout_list
            await asyncio.wait_for(task, timeout=timeout_list[i])
            # Получение результата выполнения корутины
            result = task.result()
            # Вывод результата выполнения корутины с указанием индекса задачи
            print(f"Результат выполнения корутины {i}: {result}")
        except asyncio.TimeoutError:
            # Обработка исключения при превышении времени ожидания завершения задачи
            print(
                f"Задача {i} не была завершена в указанное время (таймаут: {timeout_list[i]} сек.).")

asyncio.run(main())
