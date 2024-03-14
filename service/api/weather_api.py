from fastapi import APIRouter
from service.configuration.properties_manager import PropertiesManager
from ..request.request_service import RequestManager


router = APIRouter()
propertiesManager = PropertiesManager()


@router.get("/")
def get_weather_for_now(city: str = propertiesManager.read_property("default.city")):
    requestManager = RequestManager()
    arguments = {"q": city, "appid": propertiesManager.read_property("appid")}
    response = requestManager.perform_get_request(
        requestManager.add_arguments_to_url(propertiesManager.read_property("weather.url"), arguments))
    return f'Response Body: {response.data.decode("utf-8")}'
