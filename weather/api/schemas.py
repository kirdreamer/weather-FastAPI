from pydantic import BaseModel


class Weather(BaseModel):
    temperature: float
    status: str