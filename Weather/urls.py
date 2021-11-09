from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather, name='weather'),
    path('weatherForecast/', views.weatherForecast, name='weatherForecast'),
]
