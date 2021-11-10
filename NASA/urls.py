from django.urls import path
from . import views
urlpatterns = [
    path('', views.NASA, name='NASA'),
]
