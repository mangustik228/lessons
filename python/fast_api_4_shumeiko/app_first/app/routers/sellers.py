from fastapi import APIRouter
from app.models.dao import SellerDAO
from app.schemas.sellers import SSeler

router = APIRouter(prefix='/seller')


@router.get('s', response_model=list[SSeler])
async def get_sellers():
    return await SellerDAO.find_all()
