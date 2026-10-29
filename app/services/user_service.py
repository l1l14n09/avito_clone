from sqlalchemy.orm import Session
from app.repositories.user_repo import UserRepository
from app.schemas.user import UserCreate
from app.models.user import User

class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def register_user(self, data: UserCreate) -> User:

        return self.repo.create(username=data.username, email=data.email)

    def get_user(self, user_id: int) -> User:
        user = self.repo.get_by_id(user_id)
        if not user:
            raise ValueError("Пользователь не найден")
        return user