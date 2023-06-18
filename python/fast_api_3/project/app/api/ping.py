import random
from fastapi import APIRouter, Depends
from app.config import get_settings, Settings


router = APIRouter()


@router.get('/ping')
async def ping(settings: Settings = Depends(get_settings)):
    return {
        "status": "ok",
        "ping": "pong",
        "debug": settings.debug
    }


@router.get('/data')
async def get_data_with_delay():
    val = random.random()
    return {
        "status": "ok",
        "sleep": val
    }
