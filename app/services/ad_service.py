from sqlalchemy.orm import Session
from app.repositories.ad_repo import AdRepository
from app.repositories.user_repo import UserRepository
from app.schemas.ad import AdCreate
from app.models.ad import Ad


class AdService:
    def __init__(self, db: Session):
        self.ad_repo = AdRepository(db)
        self.user_repo = UserRepository(db)

    def create_ad(self, data: AdCreate) -> Ad:

        user = self.user_repo.get_by_id(data.user_id)
        if not user:
            raise ValueError("Автор объявления не найден")

        return self.ad_repo.create(data.model_dump())