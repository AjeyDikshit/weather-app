from django.shortcuts import render, HttpResponse, redirect
import requests
from .models import Citie

with open('API_KEY', 'r') as file:
    access_key = file.read()

# TODO: static files not loading

def home(request):
    if request.method == 'GET':
        cities = Citie.objects.all()

        weather_data = []

        for city in cities:
            city_temp = Citie.objects.get(name=city).id
            data = requests.get(f"http://api.weatherstack.com/current?access_key={access_key}&query={city}").json()
            weather_info = dict(city_id=city_temp,
                                img_src=data['current']['weather_icons'][0],
                                city_name=data['location']['name'],
                                country=data['location']['country'],
                                localtime=data['location']['localtime'],
                                temperature=data['current']['temperature'],
                                description=data['current']['weather_descriptions'][0],
                                feels_like=data['current']['feelslike'],
                                visibiltity=data['current']['visibility'],
                                humidity=data['current']['humidity'],
                                wind_speed=data['current']['wind_speed']
                                )
            weather_data.append(weather_info)
        context = {'weather_data': weather_data}

        return render(request, 'base.html', context)

    if request.method == 'POST':
        city = request.POST['city']
        Citie.objects.create(name=city)

        return redirect("home")

def delete_record(request, id):
    delete_it = Citie.objects.get(id=id)
    delete_it.delete()
    return redirect("home")

def home1(request, city):
    data = requests.get(f"http://api.weatherstack.com/current?access_key={access_key}&query={city}").json()

    weather_info = dict(img_src=data['current']['weather_icons'][0],
                        city_name=data['location']['name'],
                        country=data['location']['country'],
                        localtime=data['location']['localtime'],
                        temperature=data['current']['temperature'],
                        description=data['current']['weather_descriptions'][0],
                        feels_like=data['current']['feelslike'],
                        visibiltity=data['current']['visibility'],
                        humidity=data['current']['humidity'],
                        wind_speed=data['current']['wind_speed']
                        )
    print(weather_info)

    return render(request, "view.html", weather_info)