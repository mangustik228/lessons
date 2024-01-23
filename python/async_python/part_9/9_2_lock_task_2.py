import asyncio
import random

# Общий ресурс - база данных
database = []
Schritt = 0

lock = asyncio.Lock()

# Функция для записи данных в базу данных


async def write_to_database(data):
    # Имитация длительной операции записи
    await asyncio.sleep(random.randint(1, 3))
    global Schritt
    if Schritt == 2 or Schritt == 5:
        bonus = f", Счастливый номер! Бонус клиента = номер клиента {Schritt} * 100 == {Schritt*100}"
        data = data + bonus
    Schritt += 1
    database.append(data)


# Асинхронная функция для обработки запросов клиентов
async def handle_request(client_id):
    data = f"Data от клиента {client_id}"

    # Критический участок кода, требующий синхронизации
    async with lock:
        await write_to_database(data)
    print(f"Data от клиента {client_id} успешно записан в базу данных")


# Создание и запуск корутин для обработки запросов от клиентов
async def main():
    tasks = []

    # Измените функцию

    for i in range(10):
        tasks.append(handle_request(i))
    await asyncio.gather(*tasks)


# Запуск основной асинхронной функции
asyncio.run(main())

print(*database, sep="\n")
