

import asyncio


async def main():
    queue = asyncio.Queue()
    print(f"{queue.empty() = }")
    await queue.put(5)
    print(f"{await queue.get() = }")

if __name__ == '__main__':
    asyncio.run(main())
