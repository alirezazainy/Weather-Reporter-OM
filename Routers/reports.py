from fastapi import APIRouter, Depends, HTTPException, Security
from Controller.daily import catch_daily_data
from Controller.hourly import catch_hourly_data
from sqlalchemy.orm import Session
from Controller.responses import daily_by_location, hourly_by_location
from DB.database import get_db
from authorization import get_current_user
from schemas import RequestBaseModel, UserBase
# Reports router

router = APIRouter(prefix="/reports", tags=['Reports'])


@router.post("/daily")
async def daily(request: RequestBaseModel, user: UserBase = Security(get_current_user), db: Session = Depends(get_db)):
    """
    Get result of saving daily report operation
    
    Inputs: 
    request.latitude -> latitude of the location
    request.longitude -> longitude of location 
    request.forecast_days -> if true give results of 16 days else 7 days (default as False)

    Output:
    A json response from data you want
    """
    # saving response from catch_daily_data method 
    response = catch_daily_data(request, db, user)
    return response
    
@router.post("/hourly")
async def hourly(request: RequestBaseModel, user: UserBase = Security(get_current_user), db: Session = Depends(get_db)):
    """
    Get result of saving hourly report operation

    Inputs:
    request.latitude -> latitude of the location
    request.longitude -> longitude of location 
    request.forecast_days -> if true give results of 16 days else 7 days (default as False)

    Output:
    A json response from data you want
    """
    # saving response from catch_hourly_data method
    response = catch_hourly_data(request, db, user)
    if response == 202:
        data = hourly_by_location(request, user, db)
        _dict = {
            "data": data
        }
        return _dict
