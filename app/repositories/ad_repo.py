from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.ad import Ad

class AdRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, ad_data: dict) -> Ad:
        ad = Ad(**ad_data)
        self.db.add(ad)
        self.db.commit()
        self.db.refresh(ad)
        return ad

    def get_all(self) -> list[Ad]:
        return list(self.db.scalars(select(Ad)).all())