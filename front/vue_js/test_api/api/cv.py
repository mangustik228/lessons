from fastapi import (APIRouter, Depends, Request, UploadFile, File)
from loguru import logger
import models.pydantic as pyd
from models import crud
from models.db import get_session


router = APIRouter()


@router.get('/types', response_model=pyd.CvTypesSchema)
def get_types():
    return pyd.CvTypesSchema()


async def get_image_from_post_request(request: Request):
    ...


@router.post("/images/{user_id}")
async def post_image(
    user_id: int,
    avatar: UploadFile = File(...),
    session=Depends(get_session)
):

    logger.debug(f'post image')
    is_new, user_id = await crud.post_image(avatar, user_id, session)
    return {
        "status": "ok",
        "is_new": "created" if is_new else "updated",
        "user_id": user_id
    }


@router.get('/text/{user_id}', response_model=pyd.TextResponse)
async def get_all_text_by_id(user_id: int, session=Depends(get_session)) \
        -> pyd.TextResponse:
    data = await crud.get_texts(user_id, session)
    logger.debug(f'{data = }')
    result = {
        "status": "ok",
        "user_id": user_id,
        "data": data
    }
    logger.debug(result)
    return result


@router.post('/text')
async def get_types(data: pyd.CvPostRequest, session=Depends(get_session)):
    is_new, result = await crud.post_text(data, session)

    return {
        "status": "ok",
        "new_id": result,
        "is_new": 'created' if is_new else "updated"
    }
