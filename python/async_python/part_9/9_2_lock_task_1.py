import asyncio

robot_names = ['Электра', 'Механикс', 'Оптимус', 'Симулакр', 'Футуриус']

lock = asyncio.Lock()

counter = 0


async def move_to_A(robot_id, robot_name):
    global counter
    print(f"Робот {robot_name}({robot_id}) передвигается к месту A")
    async with lock:
        counter += 1
        print(
            f"Робот {robot_name}({robot_id}) достиг места A. Место A посещено {counter} раз")


async def main():
    tasks = [asyncio.create_task(move_to_A(i, name))
             for i, name in enumerate(robot_names)]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
