from DB.models import Daily, Hourly
from sqlalchemy.orm import Session
from fastapi import HTTPException
from Modules.datacatcher import data_catcher
from schemas import RequestBaseModel, DailyBase, UserBase
from datetime import datetime
# Data getting Controller

# TODO: Data by time

def get_all_data(user: UserBase, db: Session):
    """
    getting all user data from database
    """
    try:
        daily_data = db.query(Daily).filter(Daily.user_id == user.id).all()
        hourly_data = db.query(Hourly).filter(Hourly.user_id == user.id)
        return [daily_data, hourly_data]
    except HTTPException:
        HTTPException(404, "not found")

def daily_by_location(request: RequestBaseModel, user: UserBase, db: Session):
    """
    """
    pass

def hourly_by_location(request: RequestBaseModel, user: UserBase, db: Session):
    pass

def all_by_location(request: RequestBaseModel, user: UserBase, db: Session):
    pass

