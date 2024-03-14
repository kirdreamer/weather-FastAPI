from fastapi import FastAPI
from service.api.weather_api import router as weather_router


app = FastAPI()


app.include_router(weather_router, prefix="/weather")
