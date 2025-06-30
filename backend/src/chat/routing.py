from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from chat.models import ChatMessagePayload, ChatMessage, ChatMessageListItem
from api.db import get_session

from ai.schemas import EmailMessageSchema
from ai.services import generate_email_message

router = APIRouter()

@router.get("/")
async def chat_health():
    return {"message": "Hello, FASTAPI again!"}

# curl http://localhost:8000/api/chat/recent/
@router.get("/recent/", response_model=List[ChatMessageListItem])
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage)
    results = session.exec(query).fetchall()[:10]
    return results

# curl -X POST -d '{"message": "Give me a summary of why it is good to go outside"}' -H "Content-Type: application/json" http://localhost:8000/api/chat/
# curl -X POST -d '{"message": "Give me a summary of why it is good to go outside"}' -H "Content-Type: application/json" https://docker-ai-agent-python-production-0067.up.railway.app/api/chat/
@router.post("/", response_model=EmailMessageSchema)
def chat_create_message(payload: ChatMessagePayload, session: Session = Depends(get_session)):
    data = payload.model_dump()
    print(data)
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)

    response = generate_email_message(payload.message)
    return response
