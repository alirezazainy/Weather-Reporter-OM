from fastapi import APIRouter, Depends, HTTPException
from Controller.daily import catch_daily_data
from sqlalchemy.orm import Session
from DB.database import get_db
from schemas import RequestBaseModel
# Reports router

router = APIRouter(prefix="/reports", tags=['Reports'])


@router.post("/daily")
async def report(request: RequestBaseModel, db: Session = Depends(get_db)):
    response = catch_daily_data(request, db)
    if response == 202:
        raise HTTPException(202, 'Objects Accepted')