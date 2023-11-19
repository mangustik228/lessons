

import asyncio
from random import random


class MyAsyncGenerator:
    def __init__(self, n: int):
        self.data = [*range(n)]

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            await asyncio.sleep(random())
            return self.data.pop(0)
        except IndexError:
            raise StopAsyncIteration


async def main():
    async for i in MyAsyncGenerator(5):
        print(i)


if __name__ == '__main__':
    asyncio.run(main())
