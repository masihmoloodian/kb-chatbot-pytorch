from fastapi import APIRouter
from src.services.chat_service import ChatService

router = APIRouter(prefix="/chat")

service = ChatService()


@router.get("")
def chat():
    return service.chat()
