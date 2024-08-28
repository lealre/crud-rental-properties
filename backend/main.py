from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.database import engine
from backend.model import table_registry
from backend.router import router


app = FastAPI()

@app.get('/')
def get_root():
    return {'message': 'Hello World!'}


app.include_router(router)
