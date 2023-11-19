from collections import namedtuple
import asyncio
import random

ip_address = "192.168.0.1"
ports = namedtuple('port', ["min", "max"])(80, 85)


async def scan_port(address: str, port: int):
    await asyncio.sleep(1)
    if random.choice([True, False]):
        print(f"Порт {port} на адресе {address} открыт")
        return port


async def scan_range(address, start_port, end_port):
    print(
        f'Сканирование портов с {start_port} по {end_port} на адресе {address}')
    tasks = []
    for port in range(start_port, end_port + 1):
        task = asyncio.create_task(scan_port(address, port))
        tasks.append(task)
    result = await asyncio.gather(*tasks)
    open_ports = filter(lambda r: r, result)
    if open_ports:
        print(f"Открытые порты на адресе {address}: {[*open_ports]}")
    else:
        print(f"Открытых портов на адресе {address} не найдено")


async def main():
    await scan_range(ip_address, ports.min, ports.max)
    print(type(ports))

if __name__ == '__main__':
    asyncio.run(main())
