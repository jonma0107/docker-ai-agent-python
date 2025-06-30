from fastapi import FastAPI
from contextlib import asynccontextmanager

from api.db import init_db
from chat.routing import router as chat_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

fastapi_app = FastAPI(lifespan=lifespan)

fastapi_app.include_router(chat_router, prefix="/api/chat")

@fastapi_app.get("/")
def read_index():
    return {"message": "Hello, world!"}

