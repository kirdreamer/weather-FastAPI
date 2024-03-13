from fastapi import APIRouter
from main import propertiesManager
from request.request_service import RequestManager


router = APIRouter()


@router.get("/")
def get_weather_for_now():
    arguments = {"q": propertiesManager.read_property("city"), "appid": propertiesManager.read_property("appid")}
    response = RequestManager.performGetRequest(
        RequestManager.addArgumentsToUrl(propertiesManager.read_property("weather.url"), arguments))
    print(response.status())
    print(f'Response Body: {response.data.decode("utf-8")}')