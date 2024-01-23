import asyncio


def foo():
    raise ValueError("hello world")


async def main():
    try:
        await asyncio.to_thread()
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    asyncio.run(main())
