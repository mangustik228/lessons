import asyncio

# Функция "производителя"
async def producer():
    future = asyncio.Future()  # Создаем экземпляр Future
    await asyncio.sleep(2)  # Имитация долгой операции
    future.set_result('Future is done!')  # Устанавливаем результат Future
    return future

# Функция "потребителя"
async def consumer():
    future = await producer()  # Ждем Future от производителя
    print(await future)  # Получаем результат Future и выводим его


asyncio.run(consumer())