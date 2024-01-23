import asyncio


async def sensor_id_124(_event, id_sm, happy_event):
    ...


async def speech_synt(bot, message):
    ...


async def robot_reaction(event: asyncio.Event, bot, message):
    await event.wait()
    await speech_synt(bot, message)


async def _event(id, id_sm, event: asyncio.Event):
    if id == id_sm:
        await asyncio.sleep(2)
        event.set()
    else:
        print('Спокойно, ждем сержанта!')


async def birthday():
    id_sm = 'sms_62933d018e09401bb61c3e823bdb4477'
    id_bots = ["d234", "d235", "d236", "d237", "d238", "d239", "d240", "d241"]
    message = "Повелитель механизмов! Долгих лет! Ты ведешь нас! Слава сержанту! Ура!"
    happy_event = asyncio.Event()
    tasks = [asyncio.create_task(robot_reaction(
        happy_event, bot, message)) for bot in id_bots]
    await sensor_id_124(_event, id_sm, happy_event)
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(birthday())
