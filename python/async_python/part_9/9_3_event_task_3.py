import asyncio
import random

error = None
count = 0
sek = 0


async def monitor_rocket_launches(interrupt_flag: asyncio.Event):
    global count
    global error
    global sek
    try:
        while True:
            error = random.choices([True, False], [0.25, 0.75])[0]
            if error or count == 500:
                interrupt_flag.set()
                break
            print(
                f"Мониторинг ракетных запусков... (Запуск номер {count} прошёл успешно)")
            count += 1
            sek += 1
            await asyncio.sleep(1)
        # Допишите сюда цикл
    finally:
        print(f"Завершение мониторинга ракетных запусков")
        # Поместите сообщение о завершении мониторинга


async def main():
    global error
    global count
    global sek
    interrupt_flag = asyncio.Event()

    task = asyncio.create_task(monitor_rocket_launches(interrupt_flag))
    # Создайте Task задачу
    while True:
        await asyncio.sleep(5)
        if interrupt_flag.is_set():
            break
        print(
            f"Время ожидания составило {sek} секунд. За это время ошибки не произошло")
    print(f"""Ошибка при запуске произошла на {sek} секунде =(
Отмена мониторинга ракетных запусков...""")
    await task

    # Допишите сюда цикл

    # Запустите созданную корутину в пункте 2 через await

if __name__ == "__main__":
    asyncio.run(main())
