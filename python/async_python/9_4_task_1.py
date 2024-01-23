import asyncio

condition = asyncio.Condition(asyncio.Lock())
users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eva',
         'Frank', 'George', 'Helen', 'Ivan', 'Julia']


async def connection(user):
    async with condition:
        print(f"Пользователь {user} ожидает доступа к базе данных")
        await condition.wait()
        print(f"Пользователь {user} подключился к БД")
        print(f"Пользователь {user} отключается от БД")


async def producer():
    async with condition:
        condition.notify_all()


async def main():
    tasks = [connection(user) for user in users]
    await asyncio.gather(*tasks, producer())

if __name__ == '__main__':
    asyncio.run(main())
