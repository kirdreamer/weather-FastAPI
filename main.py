from fastapi import FastAPI
from service.configuration.config_parser import PropertiesManager
from service.api.weather_api import router as weather_router


app = FastAPI()
propertiesManager = PropertiesManager()


app.include_router(weather_router, prefix="/weather")
