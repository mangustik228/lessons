import aiofiles 
import asyncio
import time 
from random import randint



def my_timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'Время выполнения {func.__name__:15}: {start-end}')
        return result
    return wrapper

@my_timer
async def main():
    async with aiofiles.open('example.txt', 'r') as f:
        content = await f.read()
    print(f'succesful: read file, {len(content) = }')


asyncio.run(main())


@my_timer
async def write_numbers():
    async with aiofiles.open('100_000_async.txt', mode="a") as file:
        for x in range(1,200_000):
            await file.writelines(str(randint(10000, 100000)) + '\n')

asyncio.run(write_numbers())


@my_timer
async def gen_numbers():
    async with aiofiles.open('100_000_async.txt', mode='r') as file:
        data = await file.readlines()
        file.readline()
        print(f'Длина считанного файла(method:readlines): {len(data)}')
        print(f'Тип полученного файла(method:readlines): {type(data)}')

asyncio.run(gen_numbers())


@my_timer
async def gen_numbers_readline():
    async with aiofiles.open('100_000_async.txt', mode='r') as file:
        data = await file.readline()
        print(f'Длина считанного файла(method:readline): {len(data)}')
        print(f'Тип полученного файла(method:readline): {type(data)}')

asyncio.run(gen_numbers_readline())