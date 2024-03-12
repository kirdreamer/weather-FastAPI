from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def get_weather_for_now():
    return None
