import httpx
from fastapi import APIRouter

from weather.configuration.properties_manager import PropertiesManager

router = APIRouter()
propertiesManager = PropertiesManager()


@router.get("/")
def get_weather_for_now(city: str):
    arguments = {"q": city, "appid": propertiesManager.read_property("appid")}
    response = httpx.get(propertiesManager.read_property("weather.url"), params=arguments)
    return f'Response Body: {response.json()}'
