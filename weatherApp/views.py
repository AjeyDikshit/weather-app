from django.shortcuts import render, HttpResponse
import requests

# access_key = "902c5fbb138e2b150abf57eabff54ac5"
def home(request):
    # request1 = requests.get(f"http://api.weatherstack.com/current?access_key={access_key}&query=New York")
    # print(request1.json())
    return render(request, 'base.html')