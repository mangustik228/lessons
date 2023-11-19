

import asyncio


class TestManager:
    async def __aenter__(self):
        print("open context")
        await asyncio.sleep(2)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("finish context")


async def main():
    async with TestManager():
        ...


if __name__ == '__main__':
    asyncio.run(main())
