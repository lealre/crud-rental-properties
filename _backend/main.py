from fastapi import FastAPI
from .database import engine
from .models import Base
from .router import router

Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(router)