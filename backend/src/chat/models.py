from datetime import datetime, timezone
from sqlmodel import Field, SQLModel, DateTime

def get_utc_time():
    return datetime.now().replace(tzinfo=timezone.utc)


class ChatMessagePayload(SQLModel):
    message: str


class ChatMessage(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    message: str
    created_at: datetime = Field(default_factory=get_utc_time, sa_type=DateTime(timezone=True), primary_key=False, nullable=False,)


class ChatMessageListItem(SQLModel):
    id: int | None = Field(default=None)
    message: str
    created_at: datetime = Field(default=None)

