from app.config.config import get_settings
from fastapi import FastAPI
import app.routers as routers


app = FastAPI()


app.include_router(routers.users.router)
app.include_router(routers.booking.router)
app.include_router(routers.sellers.router)


@app.get('/home')
def home():
    return {'status': 'ok'}


print(get_settings())
