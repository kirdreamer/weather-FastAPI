from fastapi import APIRouter
from service.configuration.config_parser import PropertiesManager
from ..request.request_service import RequestManager


router = APIRouter()
propertiesManager = PropertiesManager()


@router.get("/")
def get_weather_for_now():
    requestManager = RequestManager()
    arguments = {"q": propertiesManager.read_property("city"), "appid": propertiesManager.read_property("appid")}
    response = requestManager.performGetRequest(
        requestManager.addArgumentsToUrl(propertiesManager.read_property("weather.url"), arguments))
    if response.status != 200:
        #TODO CustomException
        raise 
    return f'Response Body: {response.data.decode("utf-8")}'