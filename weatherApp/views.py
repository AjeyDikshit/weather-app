from django.shortcuts import render, HttpResponse
import requests

access_key = "902c5fbb138e2b150abf57eabff54ac5"


def home(request):
    # request1 = requests.get(f"http://api.weatherstack.com/current?access_key={access_key}&query=New York")
    # data = request1.json()
    data = dict(request={'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'},
                location={'name': 'New York', 'country': 'United States of America', 'region': 'New York',
                          'lat': '40.714', 'lon': ' - 74.006', 'timezone_id': 'America / New_York',
                          'localtime': '2024 - 01 - 03 10: 06', 'localtime_epoch': 1704276360,
                          'utc_offset': ' - 5.0'},
                current={'observation_time': '03:06 PM', 'temperature': 2, 'weather_code': 113,
                         'weather_icons': [
                             'https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png'],
                         'weather_descriptions': ['Sunny'], 'wind_speed': 4, 'wind_degree': 286, 'wind_dir': 'WNW',
                         'pressure': 1018, 'precip': 0, 'humidity': 62, 'cloudcover': 0, 'feelslike': -2,
                         'uv_index': 2, 'visibility': 16, 'is_day': 'yes'})

    return render(request, 'base.html', data)
