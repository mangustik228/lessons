import asyncio
import aiohttp


# Определяем асинхронную функцию для отправки запроса и получения ответа
async def fetch(url):
    # Создаем асинхронную сессию HTTP-клиента
    async with aiohttp.ClientSession() as session:
        # Отправляем асинхронный GET-запрос и получаем ответ
        async with session.get(url) as response:
            # Возвращаем url и первые 60 символов текста ответа
            return url, (await response.text())[:60]


# Определяем главную асинхронную функцию
async def main():
    # Список URL-адресов для отправки запросов
    urls = [
        'https://www.example.com/',
        'https://www.google.com/',
        'https://www.github.com/',
        'https://www.gddddd.com/'

    ]
    tasks = []  # Создаем пустой список для хранения задач
    for url in urls:  # Для каждого URL-адреса в списке
        # Устанавливаем защиту от отмены для fetch, добавляем в список задач
        task = asyncio.shield(fetch(url))
        tasks.append(task)
    # Дожидаемся выполнения всех задач и сохраняем результаты в список responses
    responses = await asyncio.gather(*tasks, return_exceptions=True)

    for response in responses:  # Выводим результаты для каждого ответа
        if isinstance(response, Exception):
            # Если ответ является исключением, выводим ошибку
            print(f"Ошибка: {response}")
        else:  # Если ответ успешный, выводим url и начальные 50 символов текста ответа
            print(f"Успешный ответ: {response}")


asyncio.run(main())  # Запускаем асинхронную главную функцию
