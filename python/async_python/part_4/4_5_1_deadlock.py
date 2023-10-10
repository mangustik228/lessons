import asyncio

# Пример deadlock когда сразу дважды идет обращение к одному mutex

lock = asyncio.Lock()


async def foo():
    print('before: Block1')
    async with lock:
        print('before: Block2')
        async with lock:
            print('main code')


async def main():
    await foo()

if __name__ == '__main__':
    asyncio.run(main())
