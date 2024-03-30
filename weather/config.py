import os
from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class AppConfig:
    app_id: str
    weather_url: str


def load_from_env() -> AppConfig:
    return AppConfig(
        app_id=os.environ["WEATHER_APP_ID"],
        weather_url=os.environ["WEATHER_URL"]
    )