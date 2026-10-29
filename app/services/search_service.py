from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.ad import Ad

class SearchService:
    def __init__(self, db: Session):
        self.db = db

    def search_ads(self, query: str) -> list[Ad]:

        stmt = select(Ad).where(Ad.title.contains(query))
        return list(self.db.scalars(stmt).all())