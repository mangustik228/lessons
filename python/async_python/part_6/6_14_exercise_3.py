import asyncio
from collections import namedtuple
import random

ip_addresses = [
    '192.168.0.1', '192.168.0.2', '192.168.0.3', '192.168.0.4',
    '192.168.0.5', '192.168.0.6', '192.168.0.7', '192.168.0.8',
    '192.168.0.9', '192.168.0.10', '192.168.1.1', '192.168.1.2',
    '192.168.1.3', '192.168.1.4', '192.168.1.5', '192.168.1.6',
    '192.168.1.7', '192.168.1.8', '192.168.1.9', '192.168.1.10',
    '192.168.2.1', '192.168.2.2', '192.168.2.3', '192.168.2.4',
    '192.168.2.5'
]

ports = namedtuple("ports", ["start", "end"])(0, 300)


async def scan_port(address: str, port: int):
    await asyncio.sleep(1)
    is_open = False if random.randint(0, 99) else True
    if is_open:
        print(f"Port {port} on {address} is open")
        return address, port


async def scan_range(address, start_port, end_port):
    print(f"Scanning ports {start_port}-{end_port} on {address}")

    tasks = []
    for port in range(start_port, end_port + 1):
        task = asyncio.create_task(scan_port(address, port))
        tasks.append(task)
    result = await asyncio.gather(*tasks)
    openning_ports = [*filter(lambda r: r, result)]
    return address, openning_ports


async def main():
    tasks = []

    for ip_address in ip_addresses:
        task = asyncio.create_task(scan_range(
            ip_address, ports.start, ports.end))
        tasks.append(task)

    data = await asyncio.gather(*tasks)

    for datum in data:
        if datum[1]:
            print(
                f"Всего найдено открытых портов {len(datum[1])} для ip: {datum[0]}")
        else:
            print(f"No open ports on {datum[0]}")

if __name__ == '__main__':
    asyncio.run(main())
