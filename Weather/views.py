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
        print(response.json())
        return render(request, 'Weather/weather.html', context)
    else:

        return render(request, 'Weather/weather.html', context)


def weatherForecast(request):
    district = request.POST.get('selectDistrict')
    print(district)
    return HttpResponse(district)