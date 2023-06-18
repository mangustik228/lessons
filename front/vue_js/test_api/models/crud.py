import os
from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger
import models.pydantic as pyd
from models.db import DatabaseCv
from sqlalchemy.future import select
import aiofiles


async def post_text(data: pyd.CvPostRequest, session: AsyncSession) -> int:
    stmt = select(DatabaseCv).\
        where(DatabaseCv.user_id == data.user_id,
              DatabaseCv.title == data.type_)
    result = await session.execute(stmt)
    cv_model = result.scalar()
    if cv_model:
        cv_model.text = data.data
        logger.info(f'Обновил данные о {data.user_id}')
        is_new = False
    else:
        cv_model = DatabaseCv(
            user_id=data.user_id,
            title=data.type_,
            text=data.data
        )
        session.add(cv_model)
        logger.info(f'Добавил данные о {data.user_id}')
        is_new = True
    await session.commit()
    await session.refresh(cv_model)
    return is_new, cv_model.id


async def get_texts(user_id: int, session: AsyncSession):
    stmt = select(DatabaseCv.title, DatabaseCv.text)\
        .where(DatabaseCv.user_id == user_id)
    result = await session.execute(stmt)
    return result.mappings().all()


async def post_image(avatar: UploadFile, user_id: int, session: AsyncSession):
    filename = f"{user_id}_{avatar.filename}"
    filepath = os.path.join('./images', filename)
    logger.debug(f'{filepath = }')
    async with aiofiles.open(filepath, 'wb') as file:
        picture = await avatar.read()
        await file.write(picture)
        logger.debug(f'picture saved: {filepath}')
    result = pyd.CvPostRequest(
        type_="Аватар",
        data=filepath,
        user_id=user_id)
    logger.debug(f'{result}')
    return await post_text(result, session)
