from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.search_service import SearchService
from app.schemas.ad import AdResponse

router = APIRouter(prefix="/search", tags=["Search"])

@router.get("/", response_model=list[AdResponse])
def search(q: str, db: Session = Depends(get_db)):
    service = SearchService(db)
    return service.search_ads(q)