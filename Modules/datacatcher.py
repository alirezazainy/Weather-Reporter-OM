from fastapi.encoders import jsonable_encoder
import requests
import json
#Catching data from open-meteo.com




def url_generator(lon: float, lat: float, fd: bool):
    """
    This method catch data from open-meteo api

    Inputs: 
    lon -> Longitude of location
    lat -> Latitude if location
    fd -> if true forecast days will 16 else 7
    
    Output: 
    An url from open meteo
    """
    if fd:
        # forecast_days has been 16
        URL = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,relativehumidity_2m,dewpoint_2m,apparent_temperature,precipitation_probability,precipitation,rain,weathercode,pressure_msl,surface_pressure,cloudcover,cloudcover_low,cloudcover_mid,cloudcover_high,visibility,evapotranspiration,et0_fao_evapotranspiration,vapor_pressure_deficit,windspeed_10m,windgusts_10m,soil_temperature_0cm,soil_temperature_6cm,soil_temperature_18cm,soil_temperature_54cm,soil_moisture_0_1cm,soil_moisture_1_3cm,soil_moisture_3_9cm,soil_moisture_9_27cm,soil_moisture_27_81cm&daily=weathercode,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset,uv_index_max,uv_index_clear_sky_max,precipitation_sum,precipitation_hours,precipitation_probability_max,windspeed_10m_max,windgusts_10m_max,winddirection_10m_dominant,shortwave_radiation_sum,et0_fao_evapotranspiration&timezone=auto&past_days=31&forecast_days=16"
    else:
        # forecast_days has been 7
        URL = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,relativehumidity_2m,dewpoint_2m,apparent_temperature,precipitation_probability,precipitation,rain,weathercode,pressure_msl,surface_pressure,cloudcover,cloudcover_low,cloudcover_mid,cloudcover_high,visibility,evapotranspiration,et0_fao_evapotranspiration,vapor_pressure_deficit,windspeed_10m,windgusts_10m,soil_temperature_0cm,soil_temperature_6cm,soil_temperature_18cm,soil_temperature_54cm,soil_moisture_0_1cm,soil_moisture_1_3cm,soil_moisture_3_9cm,soil_moisture_9_27cm,soil_moisture_27_81cm&daily=weathercode,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset,uv_index_max,uv_index_clear_sky_max,precipitation_sum,precipitation_hours,precipitation_probability_max,windspeed_10m_max,windgusts_10m_max,winddirection_10m_dominant,shortwave_radiation_sum,et0_fao_evapotranspiration&timezone=auto&past_days=31"
    return URL


def data_catcher(lon: float, lat: float, fd: bool = False):
    """
    This method transform json to dictionary

    Inputs: 
    lon -> Longitude of location
    lat -> Latitude if location
    fd -> if true forecast days will 16 else 7 (default as False)

    Output:
    A dictionary from open meteo report
    """
    # Generate open-meteo url
    URL = url_generator(lon, lat, fd)
    # send request to url
    response = requests.get(URL)
    # translate json response to python dictionary
    dic = json.loads(jsonable_encoder(response.text))
    return dic