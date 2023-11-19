import asyncio
codes = ["56FF4D", "A3D2F7", "B1C94E", "F56A1D", "D4E6F1",
         "A1B2C3", "D4E5F6", "A7B8C9", "D0E1F2", "A3B4C5",
         "D6E7F8", "A9B0C1", "D2E3F4", "A5B6C7", "D8E9F0"]

messages = ["Привет, мир!", "Как дела?", "Что нового?", "Добрый день!", "Пока!",
            "Спокойной ночи!", "Удачного дня!", "Всего хорошего!", "До встречи!", "Счастливого пути!",
            "Успехов в работе!", "Приятного аппетита!", "Хорошего настроения!", "Спасибо за помощь!", "Всего наилучшего!"]


async def get_code(code: str):
    await asyncio.sleep(0.5)
    return code


def decode_msg(task: asyncio.Task):
    code = task.result()
    msg = messages[codes.index(code)]
    print(f"Сообщение: {msg}")
    print(f"Код: {code}")


async def main():
    tasks = []
    for code in codes:
        task = asyncio.create_task(get_code(code))
        task.add_done_callback(decode_msg)
        tasks.append(task)
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
