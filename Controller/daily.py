from DB.models import Daily
from sqlalchemy.orm import Session
from fastapi import HTTPException
from Modules.datacatcher import data_catcher
from schemas import RequestBaseModel, DailyBase
from datetime import datetime
# Daily model Unit of work


DATE_FORMAT = '%Y-%m-%d' # -> format of date in open meteo strings
DATETIME_FORMAT = '%Y-%m-%dT%H:%M' # -> format of datetime in open meteo strings


def save_data(response: DailyBase, db: Session):
    """
    This method saves response model of daily report in database

    Inputs: 
    response -> as a DailyBase class attrs
    db -> as a database session

    Output:
    nothing or HttpException with 406 Unacceptable response
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
    except HTTPException:
        raise HTTPException(406, 'Objects not Acceptable')



def catch_daily_data(request: RequestBaseModel, db: Session):
    """
    This method collapse the response dictionary
    
    Inputs:
    request -> as Request base model class attrs
    db -> as a database session

    Output:
    202 or HttpException with 406 Unacceptable response
    """
    try:
        # calling dictionary from OM
        report = data_catcher(lon=request.longitude, lat=request.latitude, fd=request.forecast_days) 
        # slicing daily part
        daily = report["daily"] 
        # slicing time part
        days = daily["time"] 
        # Generate an instance from DailyBase
        response = DailyBase
        i = 0 # -> counter
        for day in days:
            today = datetime.strptime(day, DATE_FORMAT).date() # -> transform date from string to date format
            sunrise = daily["sunrise"][i] # -> giving value for transform format
            sunset = daily["sunset"][i] # -> giving value for transform format
            response.lat = request.latitude
            response.lon = request.longitude
            response.date = today
            response.weather = daily["weathercode"][i]
            response.tempmax = daily["temperature_2m_max"][i]
            response.tempmin = daily["temperature_2m_min"][i]
            response.atempmax = daily["apparent_temperature_max"][i]
            response.atempmin = daily["apparent_temperature_min"][i]
            response.sunrise = datetime.strptime(sunrise, DATETIME_FORMAT).time() # -> transform and save value from string to date format
            response.sunset = datetime.strptime(sunset, DATETIME_FORMAT).time() # -> transform and save value from string to date format
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
            save_data(response, db) # -> saving to database 
            i += 1
        return 202       
    except HTTPException:
        raise HTTPException(406, 'Objects not Acceptable')
    
