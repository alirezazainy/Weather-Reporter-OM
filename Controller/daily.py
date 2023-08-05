from DB.models import Daily
from sqlalchemy.orm import Session
from fastapi import HTTPException
from Modules.datacatcher import data_catcher
from schemas import RequestBaseModel, DailyBase
from datetime import datetime
# Daily model Unit of work


DATE_FORMAT = '%Y-%m-%d'
DATETIME_FORMAT = '%Y-%m-%dT%H:%M'


def save_data(response: DailyBase, db:Session):
    """
    This method saves response model of daily report in database
    """
    try:
        daily = Daily(
            lat=response.lat,
            lon=response.lon,
            date=response.date,
            weather=response.weather,
            tempmax=response.tempmax,
            tempmin=response.tempmin,
            atempmax=response.atempmax,
            atempmin=response.atempmin,
            sunrise=response.sunrise,
            sunset=response.sunset,
            uvinmax=response.uvinmax,
            uicsmax=response.uicsmax,
            precipsum=response.precipsum,
            preciphours=response.preciphours,
            prepromax=response.prepromax,
            windspeed=response.windspeed,
            windgusts=response.windgusts,
            winddirection=response.winddirection,
            shortwave=response.shortwave,
            evapor=response.evapor
        )
        db.add(daily)
        db.commit()
        db.refresh(daily)
    except:
        raise HTTPException(406, 'Objects not Acceptable')


def catch_daily_data(request: RequestBaseModel, db:Session):
    """
    This method collapse the response dictionary
    """
    try:    
        report = data_catcher(lon=request.longitude, lat=request.latitude, fd=request.forecast_days)
        daily = report["daily"]
        days = daily["time"]
        response = DailyBase
        i = 0
        for day in days:
            today = datetime.strptime(day, DATE_FORMAT).date()
            sunrise = daily["sunrise"][i]
            sunset = daily["sunset"][i]
            response.lat = request.latitude
            response.lon = request.longitude
            response.date = today
            response.weather = daily["weathercode"][i]
            response.tempmax = daily["temperature_2m_max"][i]
            response.tempmin = daily["temperature_2m_min"][i]
            response.atempmax = daily["apparent_temperature_max"][i]
            response.atempmin = daily["apparent_temperature_min"][i]
            response.sunrise = datetime.strptime(sunrise, DATETIME_FORMAT).time()
            response.sunset = datetime.strptime(sunset, DATETIME_FORMAT).time()
            response.uvinmax = daily["uv_index_max"][i]
            response.uicsmax = daily["uv_index_clear_sky_max"][i]
            response.precipsum = daily["precipitation_sum"][i]
            response.preciphours = daily["precipitation_hours"][i]
            response.prepromax = daily["precipitation_probability_max"][i]
            response.windspeed = daily["windspeed_10m_max"][i]
            response.windgusts = daily["windgusts_10m_max"][i]
            response.winddirection = daily["winddirection_10m_dominant"][i]
            response.shortwave = daily["shortwave_radiation_sum"][i]
            response.evapor = daily["et0_fao_evapotranspiration"][i]
            save_data(response, db)
            i += 1
        return 202       
    except:
        raise HTTPException(406, 'Objects not Acceptable')
    
