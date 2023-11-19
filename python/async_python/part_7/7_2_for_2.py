import asyncio
import random


class AsyncCounter:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.start >= self.end:
            raise StopAsyncIteration
        self.start += 1
        await asyncio.sleep(1)
        return self.start - 1


async def main():
    async for number in AsyncCounter(1, 11):
        print(f"Generated number: {number}")

asyncio.run(main())
