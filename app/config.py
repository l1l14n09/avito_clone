from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./avito.db"
    PROJECT_NAME: str = "Avito Clone API"

settings = Settings()