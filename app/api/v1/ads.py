from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.ad_service import AdService
from app.schemas.ad import AdCreate, AdResponse

router = APIRouter(prefix="/ads", tags=["Ads"])

@router.post("/", response_model=AdResponse)
def create_ad(data: AdCreate, db: Session = Depends(get_db)):
    service = AdService(db)
    try:
        return service.create_ad(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))