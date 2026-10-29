from sqlalchemy.orm import Session
from app.models.message import Message

class MessageRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, text: str, sender_id: int, receiver_id: int) -> Message:
        msg = Message(text=text, sender_id=sender_id, receiver_id=receiver_id)
        self.db.add(msg)
        self.db.commit()
        self.db.refresh(msg)
        return msg