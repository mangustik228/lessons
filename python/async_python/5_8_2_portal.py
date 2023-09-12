import asyncio


async def foo(x: int, **kwargs):
    print(f"{kwargs['first']}, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    result = kwargs["function"](x)
    print(f"Результат {kwargs['second']}: {result} единиц {kwargs['units']}")

OPERATIONS = [
    {"function": lambda x: x * 2, "first": "Активация портала в процессе",
        "second": "активации портала", "units": "энергии"},
    {"function": lambda x: x + 2, "first": "Телепортация в процессе",
        "second": "телепортации", "units": "времени"},
    {"function": lambda x: x * 3, "first": "Подзарядка портала",
        "second": "подзарядки портала", "units": "энергии"},
    {"function": lambda x: x + 4, "first": "Проверка стабильности портала",
        "second": "проверки стабильности", "units": "времени"},
    {"function": lambda x: x * 5, "first": "Восстановление портала",
        "second": "восстановления портала", "units": "энергии"},
    {"function": lambda x: x - 1, "first": "Закрытие портала", "second": "закрытия портала", "units": "времени"}]


async def portal_operator():
    await asyncio.gather(*[asyncio.create_task(foo(x, **operation)
                                               ) for x, operation in zip(range(2, 8), OPERATIONS)])

if __name__ == '__main__':
    asyncio.run(portal_operator())
