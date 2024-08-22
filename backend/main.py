from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.database import engine
from backend.model import table_registry
from backend.router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(table_registry.metadata.create_all)
        yield
    await engine.dispose()


app = FastAPI(lifespan=lifespan)


@app.get('/')
def get_root():
    return {'message': 'Hello World!'}


app.include_router(router)
