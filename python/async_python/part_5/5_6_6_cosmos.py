import asyncio
import re

example = "#001 ps5f6537c5-506f-43c2-b095-1890ef579c52: 265 units"


async def equipment_request(request: str):
    await asyncio.sleep(1)
    num = re.search(r'(#\d+) ', request).group(1)
    return f"{num} is Ok!"


async def send_requests():
    tasks = []
    for request in equipment_list:
        tasks.append(asyncio.create_task(equipment_request(request)))
    count_requests = len(tasks)
    await asyncio.gather(*tasks)
    waiting_time = query_time()
    print(
        f"На отправку {count_requests} запросов потребовалось {waiting_time} секунд!")
