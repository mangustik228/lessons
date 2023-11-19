import asyncio


async def async_gen(n):
    for i in range(n):
        yield i
        await asyncio.sleep(1)


async def print_counter(n):
    async for number in async_gen(n):
        print(number)


async def foo():
    print("start foo")
    await asyncio.sleep(2.2)
    print(f'finish foo')


async def main():
    await asyncio.gather(print_counter(5), foo())


if __name__ == '__main__':
    asyncio.run(main())
