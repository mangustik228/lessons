from loguru import logger
from app.config.database import async_session_maker
from sqlalchemy import select
from app.models.models import Seller


class SellerDAO:
    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(Seller)
            sellers = await session.execute(query)
            result = sellers.scalars().all()
            logger.debug(f'{type(result) = }')
            return result
