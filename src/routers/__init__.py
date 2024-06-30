from fastapi import APIRouter
from src.routers import (
    chat_router,
)
from src.routers import chat_router

api_router = APIRouter()
api_router.include_router(chat_router.router, tags=["Chat"])
