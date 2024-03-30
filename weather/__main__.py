from fastapi import FastAPI

from weather.api import weather_api

app = FastAPI()


app.include_router(weather_api.router, prefix="/weather")
