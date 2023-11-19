import asyncio


async def main():
    hello = asyncio.current_task()
    print(hello.done())

if __name__ == '__main__':
    asyncio.run(main())
