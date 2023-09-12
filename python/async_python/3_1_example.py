import asyncio
import random 
from loguru import logger


async def boil_water(n):
    logger.debug(f'Ставим чайник')
    await asyncio.sleep(n)
    logger.debug(f'Чайник закипел')
    
async def cut_vegetables():
    logger.debug(f'Начинаю нарезать овощи')
    await asyncio.sleep(random.randint(1,3))
    logger.debug(f'Закончил резать овощи')
    
async def prepare_diner():
    water = asyncio.ensure_future(boil_water(4))
    vegetable = asyncio.ensure_future(cut_vegetables())
    logger.debug(type(water))
    logger.debug(type(vegetable))
    await asyncio.sleep(4.1)


    
if __name__ == '__main__':
    asyncio.run(prepare_diner())