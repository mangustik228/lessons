from fastapi import APIRouter

router = APIRouter(prefix='/booking')


@router.get('')
def booking():
    return {'status': 'booking'}
