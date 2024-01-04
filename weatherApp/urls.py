from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('', views.home),
    path('home/<str:city>/', views.home1),
]