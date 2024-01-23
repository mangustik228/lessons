import asyncio


semapthore = asyncio.Semaphore(2)


async def foo(i: int):
    async with semapthore:
        print(f"coro [{i}] ACCESS")
        await asyncio.sleep(1)


async def main():
    await asyncio.gather(*[foo(i) for i in range(8)])


if __name__ == '__main__':
    asyncio.run(main())
