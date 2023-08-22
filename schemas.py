from typing import Optional
from pydantic import BaseModel
from datetime import date, time
# Request schemas



class RequestBaseModel(BaseModel):
    """
    Requests model of location
    """
    latitude: float
    longitude: float
    forecast_days: bool = False


class DailyBase(BaseModel):
    """
    Daily Report Model
    All values names same as model Attrs names 
    """
    user_id: int
    lat: float
    lon: float
    date: date
    weather: Optional[int] = None
    tempmax: Optional[float] = None
    tempmin: Optional[float] = None
    atempmax: Optional[float] = None
    atempmin: Optional[float] = None
    sunrise: time
    sunset: time
    uvinmax: Optional[float] = None
    uicsmax: Optional[float] = None
    precipsum: Optional[float] = None
    preciphours: Optional[int] = None
    prepromax: Optional[int] = None
    windspeed: Optional[float] = None
    windgusts: Optional[float] = None
    winddirection: Optional[int] = None
    shortwave: Optional[float] = None
    evapor: Optional[float] = None


class HourlyBase(BaseModel):
    """
    Hourly Report Model
    All values names same as model Attrs names 
    """
    user_id: int
    lat: float
    lon: float
    date: date
    time: time
    temp: Optional[float] = None
    relativehumid: Optional[int] = None
    dewpoint: Optional[float] = None
    atemp: Optional[float] = None
    precipprobab: Optional[float] = None
    precip: Optional[float] = None
    rain: Optional[float] = None
    weather: Optional[int] = None
    pressure: Optional[float] = None
    srfpress: Optional[float] = None
    cloudcover: Optional[int] = None
    cldcvlow: Optional[int] = None
    cldcvmid: Optional[int] = None
    cldcvhigh: Optional[int] = None
    visibility: Optional[int] = None
    evapor: Optional[float] = None
    faoevapor: Optional[float] = None
    vpd: Optional[float] = None
    windspeed: Optional[float] = None
    windgusts: Optional[float] = None
    st: Optional[float] = None
    stsix: Optional[float] = None
    steight: Optional[float] = None
    stfifty: Optional[float] = None
    smzo: Optional[float] = None
    smot: Optional[float] = None
    smtn: Optional[float] = None
    smnt: Optional[float] = None
    smte: Optional[float] = None

class UserBase(BaseModel):
    token: str
    id: int 
    