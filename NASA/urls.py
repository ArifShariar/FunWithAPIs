from django.urls import path
from . import views
urlpatterns = [
    path('astronomy_picture_of_the_day', views.NASA_astronomy_picture_of_the_day,
         name='NASA_astronomy_picture_of_the_day'),
]
