from fastapi import FastAPI
from app.database import engine, Base
from app.config import settings


from app.models import user, ad, category, message


from app.api.v1 import users, ads, search


Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)


app.include_router(users.router, prefix="/api/v1")
app.include_router(ads.router, prefix="/api/v1")
app.include_router(search.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "API работает! Перейдите на /docs для тестирования."}