import asyncio

ip = ["192.168.0.3", "192.168.0.1", "192.168.0.2", "192.168.0.4", "192.168.0.5"]

alarm = asyncio.Event()


async def moving():
    await asyncio.sleep(2)
    print("Датчики зафиксировали движение")
    alarm.set()


async def create_sensor(id, ip):
    print(f'Датчик {id} IP-адрес {ip} настроен и ожидает срабатывания')
    await asyncio.sleep(0.5)
    await alarm.wait()
    print(f'Датчик {id} IP-адрес {ip} активирован, "Wee-wee-wee-wee"')


async def main():
    tasks = [asyncio.create_task(create_sensor(idx, i))
             for idx, i in enumerate(ip)]
    tasks.append(asyncio.create_task(moving()))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
