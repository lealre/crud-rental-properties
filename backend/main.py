from fastapi import FastAPI

from backend.router import router

app = FastAPI()


@app.get('/')
def get_root():
    return {'message': 'Hello World!'}


app.include_router(router)
