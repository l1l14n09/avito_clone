from pydantic import BaseModel

class MessageCreate(BaseModel):
    text: str
    sender_id: int
    receiver_id: int

class MessageResponse(BaseModel):
    id: int
    text: str

    class Config:
        from_attributes = True