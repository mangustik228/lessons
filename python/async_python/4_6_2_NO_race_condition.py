import asyncio


ACCOUNT = 1000
LOCK_ACCOUNT = asyncio.Lock()


async def get_money(sum: int):
    global ACCOUNT
    async with LOCK_ACCOUNT:
        if ACCOUNT >= sum:
            await asyncio.sleep(0.2)
            ACCOUNT -= sum
            print(f"Success! Снято {sum}")
        else:
            print(f'нет денег на счёте')


async def main():
    await asyncio.gather(get_money(600), get_money(800))
    print(f'Денег на счете {ACCOUNT}')

if __name__ == '__main__':
    asyncio.run(main())
