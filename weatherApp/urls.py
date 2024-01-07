from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/<str:city>/', views.home1, name='home'),
    path('delete_record/<int:id>', views.delete_record, name='delete_record'),
]