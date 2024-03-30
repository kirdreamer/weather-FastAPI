from fastapi import APIRouter

from weather import config
from weather.api.owm_client import OwmWeatherClient
from weather.api.schemas import Weather

router = APIRouter()


@router.get("/weather")
def get_weather_for_now(city: str) -> Weather:
    conf = config.load_from_env()
    owm_weather = OwmWeatherClient(conf.app_id, conf.weather_url).get_weather_in_kelvin(city)
    return Weather(temperature=owm_weather.temp)
