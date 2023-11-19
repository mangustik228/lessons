import asyncio
from itertools import product
import random

shapes = ["circle", "star", "square", "diamond", "heart"]
colors = ["red", "blue", "green", "yellow", "purple"]
actions = ["change_color", "explode", "disappear"]


async def launch_firework(shape: str, color: str, action: str):
    print(f"Запущен {color} {shape} салют, в форме {action}!!!")
    await asyncio.sleep(random.randint(1, 5))
    print(f"Салют {color} {shape} завершил выступление {action}")


async def main():
    tasks = []
    for shape, color, action in product(shapes, colors, actions):
        task = asyncio.create_task(launch_firework(shape, color, action))
        tasks.append(task)
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
