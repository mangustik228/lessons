import asyncio


async def print_message():
    while True:
        print("Имитация работы ф-ции ")
        await asyncio.sleep(1)


async def interrupt_handler(interrupt_flag: asyncio.Event):
    while True:
        await asyncio.sleep(0.5)
        if interrupt_flag.is_set():
            print(f'interrupt!')
            interrupt_flag.clear()
            break


async def main():
    interrupt_flag = asyncio.Event()
    task_1 = asyncio.create_task(print_message())
    task_2 = asyncio.create_task(interrupt_handler(interrupt_flag))
    while True:
        await asyncio.sleep(3)
        interrupt_flag.set()
        print(f'Прервал в основном цикле')
        await task_2
        task_2 = asyncio.create_task(interrupt_handler(interrupt_flag))

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
