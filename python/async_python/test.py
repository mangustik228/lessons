import asyncio


class Storage():
    def __init__(self, resource_dict: dict, ru_word: str, speed: int):
        self.resource_dict = resource_dict
        self.ru_word = ru_word
        self.speed = speed
        self.count = 0

    def get(self):
        self.count += self.speed
        print(
            f"Добыто {self.speed} ед. {self.ru_word}. На складе {self.count} ед.")


stone_resources_dict = {
    'Каменная плитка': 10,
    'Каменная ваза': 40,
    'Каменный столб': 50,
}

metal_resources_dict = {
    'Металлическая цепь': 6,
    'Металлическая рамка': 24,
    'Металлическая ручка': 54,
}

cloth_resources_dict = {
    'Тканевая занавеска': 8,
    'Тканевый чехол': 24,
    'Тканевое покрывало': 48,
}


async def gather(storage: Storage, condition: asyncio.Condition):
    while True:
        await asyncio.sleep(0.1)
        storage.get()
        async with condition:
            condition.notify()


async def craft(storage: Storage, gather_task: asyncio.Task, condition: asyncio.Condition):
    for item, value in storage.resource_dict.items():
        while True:
            async with condition:
                await condition.wait()
            if value >= storage.count:
                storage -= value
                print(f"Изготовлен {item} из {storage.ru_word}")
                break

    gather_task.cancel()


async def create_production(resource_dict: dict, word: str, speed: int):
    condition = asyncio.Condition()
    storage = Storage(resource_dict, word, speed)
    gather_task = asyncio.create_task(storage, condition)
    craft_task = asyncio.create_task(storage, gather_task, condition)
    await asyncio.gather(gather_task, craft_task)


async def main():
    await create_production(stone_resources_dict, "камня")

asyncio.run(main())
