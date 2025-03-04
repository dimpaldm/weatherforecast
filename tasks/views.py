from django.shortcuts import render
import requests
from .forms import CityForm

API_KEY = "af3f8813a03a76a8dbd20a16bc94168a"

def get_countries():
    """Fetch all countries and their cities dynamically from API"""
    url = "https://countriesnow.space/api/v0.1/countries"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["data"]
    return []

def weather_forecast(request):
    weather_data = None
    countries = get_countries()

    if request.method == "POST":
        country_name = request.POST.get("country")
        city_name = request.POST.get("city")

        if city_name:
            weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={API_KEY}"
            weather_response = requests.get(weather_url).json()

            if weather_response.get("cod") == 200:
                weather_data = {
                    "city": city_name,
                    "temperature": weather_response["main"]["temp"],
                    "description": weather_response["weather"][0]["description"],
                    "icon": weather_response["weather"][0]["icon"],
                }

    return render(request, "tasks/weather.html", {"weather_data": weather_data, "countries": countries})

# Create your views here.
