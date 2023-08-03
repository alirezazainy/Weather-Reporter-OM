from DB.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Float, Date, Time, BigInteger
# Database Tables ORM Models


class Daily(Base):
    """
    Daily Table ORM Map
    """
    __tablename__ = "Daily"
    
    ID = Column(Integer, index=True, primary_key=True)
    lat = Column(Float)
    lon = Column(Float)
    date = Column(Date)
    weather = Column(Integer, nullable=True)
    tempmax = Column(Float, nullable=True)
    tempmin = Column(Float, nullable=True)
    atempmax = Column(Float, nullable=True)
    atempmin = Column(Float, nullable=True)
    sunrise = Column(Time, nullable=True)
    sunset = Column(Time, nullable=True)
    uvinmax = Column(Float, nullable=True)
    uicsmax = Column(Float, nullable=True)
    precipsum = Column(Float, nullable=True)
    preciphours = Column(Integer, nullable=True)
    prepromax = Column(Integer, nullable=True)
    windspeed = Column(Float, nullable=True)
    windgusts = Column(Float, nullable=True)
    winddirection = Column(Integer, nullable=True)
    shortwave = Column(Float, nullable=True)
    evapor = Column(Float, nullable=True)


class Hourly(Base):
    """
    Hourly Table ORM Map
    """
    __tablename__ = "Hourly"

    ID = Column(Integer, index=True, primary_key=True)
    lat = Column(Float)
    lon = Column(Float)
    date = Column(Date)
    time = Column(Time)
    temp = Column(Float, nullable=True)
    relativehumid = Column(Integer, nullable=True)
    dewpoint = Column(Float, nullable=True)
    atemp = Column(Float, nullable=True)
    precipprobab = Column(Integer, nullable=True)
    precip = Column(Float, nullable=True)
    rain = Column(Float, nullable=True)
    weather = Column(Integer, nullable=True)
    pressure = Column(Float, nullable=True)
    srfpress = Column(Float, nullable=True)
    cloudcover = Column(Integer, nullable=True)
    cldcvlow = Column(Integer, nullable=True)
    cldcvmid = Column(Integer, nullable=True)
    cldcvhigh = Column(Integer, nullable=True)
    visibility = Column(BigInteger, nullable=True)
    evapor = Column(Float, nullable=True)
    faoevapor = Column(Float, nullable=True)
    vpd = Column(Float, nullable=True)
    windspeed = Column(Float, nullable=True)
    windgusts = Column(Float, nullable=True)
    st = Column(Float, nullable=True)
    stsix = Column(Float, nullable=True)
    steight = Column(Float, nullable=True)
    stfifty = Column(Float, nullable=True)
    smzo = Column(Float, nullable=True)
    smot = Column(Float, nullable=True)
    smtn = Column(Float, nullable=True)
    smnt = Column(Float, nullable=True)
    smte = Column(Float, nullable=True)
