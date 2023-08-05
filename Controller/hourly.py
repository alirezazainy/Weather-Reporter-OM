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
    """
    This method saves response model of hourly report in database
    """
    try:
        hourly = Hourly(
            lat=response.lat,
            lon=response.lon,
            date=response.date,
            time=response.time,
            temp=response.temp,
            relativehumid=response.relativehumid,
            dewpoint=response.dewpoint,
            atemp=response.atemp,
            precipprobab=response.precipprobab,
            precip=response.precip,
            rain=response.rain,
            weather=response.weather,
            pressure=response.pressure,
            srfpress=response.srfpress,
            cloudcover=response.cloudcover,
            cldcvlow=response.cldcvlow,
            cldcvmid=response.cldcvmid,
            cldcvhigh=response.cldcvhigh,
            visibility=response.visibility,
            evapor=response.evapor,
            faoevapor=response.faoevapor,
            vpd=response.vpd,
            windspeed=response.windspeed,
            windgusts=response.windgusts,
            st=response.st,
            stsix=response.stsix,
            steight=response.steight,
            stfifty=response.stfifty,
            smzo=response.smzo,
            smot=response.smot,
            smtn=response.smtn,
            smnt=response.smnt,
            smte=response.smte
        )
        db.add(hourly)
        db.commit()
        db.refresh(hourly)
    except:
        raise HTTPException(406, 'Objects not Acceptable')

def catch_hourly_data(request: RequestBaseModel, db: Session):
    """
    This method collapse the response dictionary
    """
    try:
        report = data_catcher(lon=request.longitude, lat=request.latitude, fd=request.forecast_days)
        hourly = report["hourly"]
        hours = hourly["time"]
        response = HourlyBase
        i = 0
        for hour in hours:
            now = datetime.strptime(hour, DATETIME_FORMAT).time()
            today = datetime.strptime(hour, DATETIME_FORMAT).date()
            response.lat = request.latitude
            response.lon = request.longitude
            response.date = today
            response.time = now
            response.temp = hourly["temperature_2m"][i]
            response.relativehumid = hourly["relativehumidity_2m"][i]
            response.dewpoint = hourly["dewpoint_2m"][i]
            response.atemp = hourly["apparent_temperature"][i]
            response.precipprobab = hourly["precipitation_probability"][i]
            response.precip = hourly["precipitation"][i]
            response.rain = hourly["rain"][i]
            response.weather = hourly["weathercode"][i]
            response.pressure = hourly["pressure_msl"][i]
            response.srfpress = hourly["surface_pressure"][i]
            response.cloudcover = hourly["cloudcover"][i]
            response.cldcvlow = hourly["cloudcover_low"][i]
            response.cldcvmid = hourly["cloudcover_mid"][i]
            response.cldcvhigh = hourly["cloudcover_high"][i]
            response.visibility = hourly["visibility"][i]
            response.evapor = hourly["evapotranspiration"][i]
            response.faoevapor = hourly["et0_fao_evapotranspiration"][i]
            response.vpd = hourly["vapor_pressure_deficit"][i]
            response.windspeed = hourly["windspeed_10m"][i]
            response.windgusts = hourly["windgusts_10m"][i]
            response.st = hourly["soil_temperature_0cm"][i]
            response.stsix = hourly["soil_temperature_6cm"][i]
            response.steight = hourly["soil_temperature_18cm"][i]
            response.stfifty = hourly["soil_temperature_54cm"][i]
            response.smzo = hourly["soil_moisture_0_1cm"][i]
            response.smot = hourly["soil_moisture_1_3cm"][i]
            response.smtn = hourly["soil_moisture_3_9cm"][i]
            response.smnt = hourly["soil_moisture_9_27cm"][i]
            response.smte = hourly["soil_moisture_27_81cm"][i]
            save_data(response, db)
            i += 1
        return 202
    except:
        raise HTTPException(406, 'Objects not Acceptable')