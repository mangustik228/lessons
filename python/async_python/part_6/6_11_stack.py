import asyncio


async def fiz(x):
    await asyncio.sleep(x)


async def bar(x):
    await fiz(x)


async def foo(x):
    await bar(x)


async def main():
    task = asyncio.create_task(foo(3))
    await asyncio.sleep(0.3)
    print(task.get_stack())
    task.print_stack()


if __name__ == '__main__':
    asyncio.run(main())
