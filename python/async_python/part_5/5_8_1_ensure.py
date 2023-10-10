import asyncio


async def activate_portal(x):
    print(f"Активация портала в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x * 2


async def perform_teleportation(x):
    print(f"Телепортация в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x + 2


async def portal_operator():
    task_activate = asyncio.ensure_future(activate_portal(2))
    time_activate = await task_activate
    task_perform_teleportation = asyncio.ensure_future(
        perform_teleportation(time_activate))
    time_teleport,  = await asyncio.gather(task_perform_teleportation)
    print(f"Результат активации портала: {time_activate} единиц энергии")
    print(f"Результат телепортации: {time_teleport} единиц времени")


if __name__ == '__main__':
    asyncio.run(portal_operator())
