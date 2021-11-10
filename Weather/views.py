import json

import requests
from django.http import HttpResponse
from django.shortcuts import render


def weather(request):
    with open('Weather/files/bd_districts.json', encoding='utf-8') as json_file:
        data = json.load(json_file)

    districts = []
    k = 0
    while k <= 63:
        districts.append(data['districts'][k]['name'])
        k += 1
    districts.sort()
    context = {'districts': districts}

    if request.POST:
        district_name = request.POST.get('selectDistrict')
        context['district_name'] = district_name
        apikey = '03c0dcc9761cb8f6c56ef511f958d11d'
        req = 'https://api.openweathermap.org/data/2.5/weather?q=' + district_name + '&units=metric&appid=' + apikey
        response = requests.get(req)
        if response.status_code == 404:
            return HttpResponse("<h1>City not available in API</h1>")
        else:
            context['lat'] = response.json()['coord']['lat']
            context['lon'] = response.json()['coord']['lon']
            context['weather_main'] = response.json()['weather'][0]['main']
            context['weather_description'] = response.json()['weather'][0]['description']
            context['temp'] = response.json()['main']['temp']
            context['temp_feels'] = response.json()['main']['feels_like']
            context['temp_min'] = response.json()['main']['temp_min']
            context['temp_max'] = response.json()['main']['temp_max']
            context['pressure'] = response.json()['main']['pressure']
            context['humidity'] = response.json()['main']['humidity']
            context['visibility'] = response.json()['visibility']
            context['wind_speed'] = response.json()['wind']['speed']
            context['wind_deg'] = response.json()['wind']['deg']
            context['clouds'] = response.json()['clouds']['all']
            return render(request, 'Weather/weather.html', context)
    else:

        return render(request, 'Weather/weather.html', context)


def weatherForecast(request):
    district = request.POST.get('selectDistrict')
    print(district)
    return HttpResponse(district)
