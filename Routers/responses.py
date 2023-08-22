import json
from fastapi import APIRouter, Depends, HTTPException, Security
from Controller.daily import catch_daily_data
from Controller.hourly import catch_hourly_data
from sqlalchemy.orm import Session
from Controller.responses import get_all_data
from DB.database import get_db
from authorization import get_current_user
from schemas import DailyBase, HourlyBase, RequestBaseModel, UserBase
# Responses router

#TODO: this router will be deleted
router = APIRouter(prefix="/responses", tags=['Responses'])


@router.post("/all")
async def get_all(user: UserBase = Security(get_current_user), db: Session = Depends(get_db)):
    model_data = get_all_data(user, db)
    data = {
        "data": [
            {
                "daily": model_data[0]
            },
            {
                "hourly": model_data[1]
            }
        ]
    }

    return data
