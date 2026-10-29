from pydantic import BaseModel

class AdCreate(BaseModel):
    title: str
    description: str | None = None
    price: int
    user_id: int
    category_id: int

class AdResponse(BaseModel):
    id: int
    title: str
    price: int
    user_id: int

    class Config:
        from_attributes = True