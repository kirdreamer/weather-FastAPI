import json
import httpx
from pydantic import BaseModel


class OwmWeather(BaseModel):
    temp: float
    main: str


class OwmWeatherClient:
    def __init__(self, app_id: str, weather_url: str) -> None:
        self.app_id = app_id
        self.weather_url = weather_url
    
    def get_weather_in_kelvin(self, city: str) -> OwmWeather:
        arguments = {"q": city, "appid": self.app_id}
        response = httpx.get(self.weather_url, params=arguments)
        data = response.json()
        return OwmWeather(temp=data["main"]["temp"], main=data["weather"][0]["main"])