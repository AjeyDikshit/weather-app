from django.shortcuts import render, HttpResponse
import requests

with open('API_KEY', 'r') as file:
    access_key = file.read()

# TODO: Add functionality to add/remove cities and give updated results whenever the user refreshes the page
# TODO: Add the entry to database and then show the data. (Can be done to solve the above TODO)

def home(request):
    if request.method == 'GET':
        return render(request, 'base.html')

    if request.method == 'POST':
        city = request.POST['city']
        data = requests.get(f"http://api.weatherstack.com/current?access_key={access_key}&query={city}").json()
        print(data)
        return render(request, 'base.html', data)

def home1(request, city):
    data = requests.get(f"http://api.weatherstack.com/current?access_key={access_key}&query={city}").json()
    print(data)
    return render(request, 'base.html', data)