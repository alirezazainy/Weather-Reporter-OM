from DB.models import Hourly
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from Modules.datacatcher import data_catcher
from schemas import RequestBaseModel, HourlyBase
from datetime import datetime
# Hourly model Unit of work

DATE_FORMAT = '%Y-%m-%d'
DATETIME_FORMAT = '%Y-%m-%dT%H:%M'

def save_data(response: HourlyBase, db: Session):
    pass

def catch_hourly_data(request: RequestBaseModel, db: Session):
    pass