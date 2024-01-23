import asyncio

storage = 0
gather = asyncio.Event()
can_created = asyncio.Condition()
wood_resources_dict = {
    'Деревянный меч': 6,
    'Деревянный щит': 12,
    'Деревянный стул': 24}


async def gather_wood():
    global storage
    while wood_resources_dict:
        need_wood = next(iter(wood_resources_dict.values()))
        await asyncio.sleep(0.5)
        storage += 2
        print(f"Добыто 2 ед. дерева. На складе {storage} ед.")
        if storage >= need_wood:
            async with can_created:
                can_created.notify()
                gather.clear()
        await gather.wait()


async def craft_item():
    global storage
    while wood_resources_dict:
        async with can_created:
            await can_created.wait()
        item = next(iter(wood_resources_dict))
        wood = wood_resources_dict.pop(item)
        storage -= wood
        print(f"Изготовлен {item}.")
        gather.set()


async def main():
    gather.set()
    await asyncio.gather(gather_wood(), craft_item())

if __name__ == '__main__':
    asyncio.run(main())
