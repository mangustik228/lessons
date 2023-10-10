import asyncio


ACCOUNT = 1000


async def withdraw_money(sum: int):
    global ACCOUNT
    if ACCOUNT >= sum:
        await asyncio.sleep(0.2)
        ACCOUNT -= sum
        print(f"Success! Снято {sum}")
    else:
        print(f'нет денег на счёте')


async def main():
    await asyncio.gather(withdraw_money(600), withdraw_money(800))
    print(f'Денег на счете {ACCOUNT}')

if __name__ == '__main__':
    asyncio.run(main())
