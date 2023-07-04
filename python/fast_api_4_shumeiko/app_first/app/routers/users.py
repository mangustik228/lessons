from fastapi import APIRouter, Depends
from loguru import logger
from app.config.database import get_session
from sqlalchemy import select
import app.models.models as models
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix='/users')


@router.get('')
async def users(session: AsyncSession = Depends(get_session)):
    query = select(models.Seller)
    result = await session.execute(query)
    logger.debug(type(result))
    logger.debug(result)
    return result.mappings().all()
