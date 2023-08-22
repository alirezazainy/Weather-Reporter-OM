from DB.database import Base
from sqlalchemy import Column, Integer, Float, Date, Time, BigInteger
# Database Tables ORM Models


class Daily(Base):
    """
    Daily Table ORM Map

    Attributes real names and their units(after lon attr) :
        "time": "iso8601",
        "weathercode": "wmo code",
        "temperature_2m_max": "°C",
        "temperature_2m_min": "°C",
        "apparent_temperature_max": "°C",
        "apparent_temperature_min": "°C",
        "sunrise": "iso8601",
        "sunset": "iso8601",
        "uv_index_max": "",
        "uv_index_clear_sky_max": "",
        "precipitation_sum": "mm",
        "precipitation_hours": "h",
        "precipitation_probability_max": "%",
        "windspeed_10m_max": "km/h",
        "windgusts_10m_max": "km/h",
        "winddirection_10m_dominant": "°",
        "shortwave_radiation_sum": "MJ/m²",
        "et0_fao_evapotranspiration": "mm"
    all of attrs respectively listed in model
    """
    __tablename__ = "Daily"
    
    ID = Column(Integer, index=True, primary_key=True)
    user_id = Column(Integer)
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

    Attributes real names and their units(after lon attr) :
        "time": "iso8601",
        "temperature_2m": "°C",
        "relativehumidity_2m": "%",
        "dewpoint_2m": "°C",
        "apparent_temperature": "°C",
        "precipitation_probability": "%",
        "precipitation": "mm",
        "rain": "mm",
        "weathercode": "wmo code",
        "pressure_msl": "hPa",
        "surface_pressure": "hPa",
        "cloudcover": "%",
        "cloudcover_low": "%",
        "cloudcover_mid": "%",
        "cloudcover_high": "%",
        "visibility": "m",
        "evapotranspiration": "mm",
        "et0_fao_evapotranspiration": "mm",
        "vapor_pressure_deficit": "kPa",
        "windspeed_10m": "km/h",
        "windgusts_10m": "km/h",
        "soil_temperature_0cm": "°C",
        "soil_temperature_6cm": "°C",
        "soil_temperature_18cm": "°C",
        "soil_temperature_54cm": "°C",
        "soil_moisture_0_1cm": "m³/m³",
        "soil_moisture_1_3cm": "m³/m³",
        "soil_moisture_3_9cm": "m³/m³",
        "soil_moisture_9_27cm": "m³/m³",
        "soil_moisture_27_81cm": "m³/m³"
    all of attrs respectively listed in model
    """
    __tablename__ = "Hourly"

    ID = Column(Integer, index=True, primary_key=True)
    user_id = Column(Integer)
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
