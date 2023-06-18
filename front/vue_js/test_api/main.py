import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api import cv


def create_app():
    app = FastAPI()
    app.include_router(cv.router, prefix="/vue")
    images_path = os.path.join(os.getcwd(), "images")
    if not os.path.exists(images_path):
        os.mkdir(images_path)
    app.mount('/images', StaticFiles(directory=images_path), name="images")
    return app


app = create_app()
