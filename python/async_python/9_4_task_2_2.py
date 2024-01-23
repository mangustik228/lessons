import asyncio

storage = 0
finish = asyncio.Event()
can_created = asyncio.Condition()
wood_resources_dict = {
    'Деревянный меч': 6,
    'Деревянный щит': 12,
    'Деревянный стул': 24}


async def gather_wood():
    global storage
    while not finish.is_set():
        storage += 2
        print(f"Добыто 2 ед. дерева. На складе {storage} ед.")
        async with can_created:
            can_created.notify()
        await asyncio.sleep(0.1)


async def craft_item():
    global storage
    for item, wood in wood_resources_dict.items():
        while True:
            async with can_created:
                await can_created.wait()
            if storage == wood:
                storage -= wood
                print(f"Изготовлен {item}.")
                break
    finish.set()


async def main():
    await asyncio.gather(gather_wood(), craft_item())

if __name__ == '__main__':
    asyncio.run(main())
